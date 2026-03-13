/**
 * SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
 * SPDX-License-Identifier: MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */

import React, {useState, useEffect} from 'react';
import * as ReactDOMClient from 'react-dom/client';
import {
    ChakraProvider,
    Box,
    Text,
    Button,
    Input,
    VStack,
    Image,
    FormLabel,
    useToast,
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    useDisclosure, Heading, Flex, HStack, IconButton, Popover,
    PopoverTrigger, PopoverContent, PopoverArrow, PopoverCloseButton,
    PopoverHeader, PopoverBody, Divider, Select, Link
} from '@chakra-ui/react';
import { LockIcon, UnlockIcon, InfoIcon, ExternalLinkIcon, ChevronDownIcon } from '@chakra-ui/icons';

import {extendTheme, ColorModeScript} from '@chakra-ui/react';
import {mode} from '@chakra-ui/theme-tools';
import SearchApp from "./HybridDeepSearchUI";
import {StyleFunctionProps} from "@chakra-ui/react";
import logo from "./img/nvidia_logo.png";
import { apiUrl as defaultApiUrl, SERVER_MAPPING, defaultEmbeddingConfig } from "./config";
import GraphVisualization from "./Graph";
import persistentCache from "./utils/persistentImageCache";
import { useDeviceFlowAuth, getServerHttpsUrl, AuthStatus, createApiToken } from "./nucleus";

const theme = extendTheme({
    colors: {
        brand: {
            50: '#76B900',
            100: '#76B900',
            200: '#76B900',
            300: '#76B900',
            400: '#76B900',
            500: '#76B900',
            600: '#76B900',
            700: '#76B900',
            800: '#76B900',
            900: '#76B900',
        },
        gray: {
            900: "#000000",
            800: "#000000",
            700: "#000000",
            600: "#000000",
            500: "#222222",
            400: "#444444",
            300: "#666666",
            200: "#888888",
            100: "#AAAAAA",
            50: "#CCCCCC",
        }
    },
    fonts: {
        heading: `'NVIDIA Sans Bold',`,
        body: `'NVIDIA Sans'`,
    },
    components: {
        Input: {
            defaultProps: {
                focusBorderColor: '#76B900',
            }
        }
    },
    shadows: {outline: '0 0 0 3px #76B900'},
    config: {
        initialColorMode: 'dark',  // Set the initial color mode to dark
        useSystemColorMode: false, // Disables the color mode switching based on the system preference
    },
    styles: {
        global: (props) => ({
            body: {
                fontFamily: 'body',
                color: mode('gray.800', 'whiteAlpha.900')(props),
                bg: 'black',
                lineHeight: 'base',
            },
        }),
    },
});

// Authentication Form Component
const AuthForm = ({ auth, setAuth, getServerStorageKey }) => {
    const [authMethod, setAuthMethod] = useState(() => {
        if (auth.username) return 'basic';
        if (auth.api_key) return 'api_key';
        return 'basic';
    });
    
    // Device flow modal state
    const { isOpen: isDeviceFlowOpen, onOpen: onDeviceFlowOpen, onClose: onDeviceFlowClose } = useDisclosure();
    const deviceFlowAuth = useDeviceFlowAuth();
    const toast = useToast();

    // Helper function to check if backend is S3
    const isS3Backend = (backendString) => {
        return backendString && backendString.toLowerCase().includes('s3');
    };

    // Helper function to check if backend is Nucleus
    const isNucleusBackend = (backendString) => {
        return backendString && backendString.toLowerCase().includes('omniverse://');
    };

    // Get backend info from HeaderIcons component
    const [backend, setBackend] = useState(null);

    // Get current server from URL params
    const [currentServer, setCurrentServer] = useState(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const serverParam = urlParams.get('server');
        const currentServer = serverParam && SERVER_MAPPING[serverParam] ? serverParam : null;
        if (currentServer) {
            return currentServer;
        }
        else {
            const servers = Object.keys(SERVER_MAPPING);
            return servers.length > 0 ? servers[0] : "";
        }
    });

    // Update currentServer when URL changes
    useEffect(() => {
        const handleServerChange = () => {
            const urlParams = new URLSearchParams(window.location.search);
            const serverParam = urlParams.get('server');
            setCurrentServer(serverParam && SERVER_MAPPING[serverParam] ? serverParam : null);
        };

        window.addEventListener('server-changed', handleServerChange);
        return () => {
            window.removeEventListener('server-changed', handleServerChange);
        };
    }, []);

    const fetchBackendInfo = async () => {
        try {
            const headers = { "Content-Type": "application/json" };
            if (auth.api_key) {
                headers["x-api-key"] = auth.api_key;
            } else if (auth.username) {
                headers["Authorization"] = `Basic ${btoa(`${auth.username}:${auth.password || ""}`)}`;
            }
            
            // Add storage backend header if a server is selected
            if (currentServer) {
                headers["x-usdsearch-storage-backend"] = currentServer;
            }
            
            const fullUrl = defaultApiUrl ? `${defaultApiUrl}/info/backend/storage` : `/info/backend/storage`;
            const response = await fetch(fullUrl, { method: 'GET', headers: headers });

            if (response.ok) {
                const data = await response.json();
                if (data.backends && Object.keys(data.backends).length > 0) {
                    const backendInfo = Object.keys(data.backends).join(', ');
                    setBackend(backendInfo);
                }
            }
        } catch (error) {
            console.error("Error fetching backend info:", error);
        }
    };

    // Fetch backend info when component mounts or server changes
    React.useEffect(() => {
        fetchBackendInfo();
    }, [auth.api_key, auth.username, auth.password, currentServer]);

    // Set default username based on backend type when server changes or backend info updates
    const setDefaultUsername = () => {
        console.log("backend", backend);
        // console.log("currentServer", currentServer);
        if (backend) {
            // Check if we have a server-specific username stored
            const serverUsername = localStorage.getItem(getServerStorageKey("username"));
            if (!serverUsername) {
                // Store the current auth state to check if we need to update
                const currentAuth = auth;
                let newUsername = null;
                let newPassword = null;
                
                if (isNucleusBackend(backend)) {
                    newUsername = '$omni-api-token';
                } else if (isS3Backend(backend)) {
                    newUsername = '';
                    newPassword = 'dummy';
                }

                // Only update if we have a new username and it's different from current
                if (newUsername !== null && newUsername !== currentAuth.username) {
                    setAuth(prevAuth => ({ ...prevAuth, username: newUsername }));
                    localStorage.setItem(getServerStorageKey("username"), newUsername);
                }
                if (newPassword !== null && newPassword !== currentAuth.password) {
                    setAuth(prevAuth => ({ ...prevAuth, password: newPassword }));
                    localStorage.setItem(getServerStorageKey("password"), newPassword);
                }
            }
        }
    }

    React.useEffect(() => {
        setDefaultUsername()
    }, [backend]);

    const handleSave = () => {
        // Save to localStorage with server-specific keys
        localStorage.setItem(getServerStorageKey("api_key"), auth.api_key || "");
        localStorage.setItem(getServerStorageKey("username"), auth.username || "");
        localStorage.setItem(getServerStorageKey("password"), auth.password || "");
        
        // Trigger storage event for other components
        const storageEvent = new StorageEvent('storage', {
            key: 'auth_updated',
            newValue: Date.now().toString()
        });
        window.dispatchEvent(storageEvent);
        
        // Also trigger a custom event for immediate update
        window.dispatchEvent(new CustomEvent('auth-updated'));
    };

    const handleClear = () => {
        localStorage.removeItem(getServerStorageKey("api_key"));
        localStorage.removeItem(getServerStorageKey("username"));
        localStorage.removeItem(getServerStorageKey("password"));
        setAuth({
            api_key: "",
            username: "",
            password: "",
        });
        window.dispatchEvent(new Event('storage'));
    };

    // Start Nucleus device flow authentication
    const handleStartDeviceFlow = async () => {
        if (!backend) {
            toast({
                title: "No server detected",
                description: "Please wait for backend information to load",
                status: "warning",
                duration: 3000,
            });
            return;
        }
        
        onDeviceFlowOpen();
        
        try {
            const result = await deviceFlowAuth.startAuth(backend);
            // Start polling for token
            deviceFlowAuth.startPolling(backend, result.device_code, result.interval);
        } catch (error) {
            toast({
                title: "Failed to start authentication",
                description: error.message,
                status: "error",
                duration: 5000,
            });
        }
    };

    // Handle successful device flow authentication - create API token
    useEffect(() => {
        const createAndSaveApiToken = async () => {
            if (deviceFlowAuth.authResult && deviceFlowAuth.authResult.status === AuthStatus.OK) {
                try {
                    // Create a long-lived API token using the access token
                    const now = new Date();
                    const timestamp = `${now.toISOString().split('T')[0]}_${now.getHours().toString().padStart(2, '0')}-${now.getMinutes().toString().padStart(2, '0')}-${now.getSeconds().toString().padStart(2, '0')}`;
                    const tokenName = `USD-Search-${timestamp}`;
                    
                    console.log("Creating API token with name:", tokenName);
                    
                    toast({
                        title: "Creating API token...",
                        description: "Please wait while we create a permanent API token",
                        status: "info",
                        duration: 3000,
                    });
                    
                    // Pass null for expireAt to create a permanent token (no expiration)
                    const apiTokenResult = await createApiToken(
                        backend, 
                        deviceFlowAuth.authResult.access_token, 
                        tokenName, 
                        null
                    );
                    
                    // Set the API token as the password with $omni-api-token username
                    const newAuth = { 
                        ...auth, 
                        username: '$omni-api-token',
                        password: apiTokenResult.api_token 
                    };
                    setAuth(newAuth);
                    
                    // Save to localStorage
                    localStorage.setItem(getServerStorageKey("username"), '$omni-api-token');
                    localStorage.setItem(getServerStorageKey("password"), apiTokenResult.api_token);
                    window.dispatchEvent(new Event('storage'));
                    window.dispatchEvent(new Event('auth-updated'));
                    
                    toast({
                        title: "Authentication successful!",
                        description: `Created permanent API token for ${deviceFlowAuth.authResult.username || 'user'}.`,
                        status: "success",
                        duration: 5000,
                    });
                    
                    onDeviceFlowClose();
                    deviceFlowAuth.reset();
                } catch (error) {
                    console.error("Failed to create API token:", error);
                    
                    toast({
                        title: "Failed to create API token",
                        description: error.message || "Unknown error occurred while creating API token",
                        status: "error",
                        duration: 8000,
                    });
                    
                    // Reset the device flow but keep the modal open so user can retry
                    deviceFlowAuth.reset();
                }
            }
        };
        
        createAndSaveApiToken();
    }, [deviceFlowAuth.authResult]);

    // Handle device flow errors
    useEffect(() => {
        if (deviceFlowAuth.error) {
            toast({
                title: "Authentication failed",
                description: deviceFlowAuth.error,
                status: "error",
                duration: 5000,
            });
        }
    }, [deviceFlowAuth.error]);

    return (
        <VStack spacing={4} align="stretch">
            <Box>
                <FormLabel fontSize="sm" mb={2}>Authentication Method</FormLabel>
                <Select size="sm" value={authMethod} onChange={(e) => setAuthMethod(e.target.value)}>
                    <option value="basic">Basic Auth</option>
                    <option value="api_key">API Key</option>
                </Select>
            </Box>

            {authMethod === 'api_key' && (
                <Box>
                    <FormLabel fontSize="sm">API Key</FormLabel>
                    <Input
                        size="sm"
                        type="password"
                        value={auth.api_key}
                        onChange={(e) => {
                            const newAuth = { ...auth, api_key: e.target.value };
                            setAuth(newAuth);
                            // Save immediately
                            localStorage.setItem(getServerStorageKey("api_key"), newAuth.api_key || "");
                            window.dispatchEvent(new Event('storage'));
                            window.dispatchEvent(new Event('auth-updated'));
                        }}
                        placeholder="Enter your API key"
                        borderColor={!auth.isAuthenticated && (!auth.api_key || auth.api_key === "") ? "red.300" : "inherit"}
                        _hover={{ borderColor: !auth.isAuthenticated && (!auth.api_key || auth.api_key === "") ? "red.400" : "inherit" }}
                        _focus={{ borderColor: !auth.isAuthenticated && (!auth.api_key || auth.api_key === "") ? "red.500" : "green.500" }}
                    />
                </Box>
            )}


            {authMethod === 'basic' && (
                <>
                    {isNucleusBackend(backend) ? (
                        <Box>
                            {auth.password ? (
                                <VStack align="stretch" spacing={2}>
                                    <Text fontSize="sm" color="green.400">
                                        ✓ Authenticated with Nucleus
                                    </Text>
                                    <Button
                                        size="sm"
                                        variant="outline"
                                        colorScheme="red"
                                        onClick={() => {
                                            const newAuth = { ...auth, username: '', password: '' };
                                            setAuth(newAuth);
                                            localStorage.setItem(getServerStorageKey("username"), "");
                                            localStorage.setItem(getServerStorageKey("password"), "");
                                            window.dispatchEvent(new Event('storage'));
                                            window.dispatchEvent(new Event('auth-updated'));
                                        }}
                                    >
                                        Clear Token
                                    </Button>
                                </VStack>
                            ) : (
                                <Button
                                    size="sm"
                                    colorScheme="green"
                                    width="100%"
                                    onClick={handleStartDeviceFlow}
                                    leftIcon={<Text>🔑</Text>}
                                >
                                    Get token from Nucleus
                                </Button>
                            )}
                        </Box>
                    ) : (
                        <>
                            <Box>
                                <FormLabel fontSize="sm">Username</FormLabel>
                                <Input
                                    size="sm"
                                    value={auth.username}
                                    onChange={(e) => {
                                        const newAuth = { ...auth, username: e.target.value };
                                        setAuth(newAuth);
                                        // Save immediately
                                        localStorage.setItem(getServerStorageKey("username"), newAuth.username || "");
                                        window.dispatchEvent(new Event('storage'));
                                        window.dispatchEvent(new Event('auth-updated'));
                                    }}
                                    placeholder="Enter username"
                                    borderColor={!auth.isAuthenticated && (!auth.username || auth.username === "") ? "red.300" : "inherit"}
                                    _hover={{ borderColor: !auth.isAuthenticated && (!auth.username || auth.username === "") ? "red.400" : "inherit" }}
                                    _focus={{ borderColor: !auth.isAuthenticated && (!auth.username || auth.username === "") ? "red.500" : "green.500" }}
                                />
                                {isS3Backend(backend) && (
                                    <Text fontSize="xs" color="gray.400" mt={1}>
                                        Please set your username - it helps us with statistics to improve the product.
                                    </Text>
                                )}
                            </Box>
                            {isS3Backend(backend) ? null : (
                            <Box>
                                <FormLabel fontSize="sm">Password</FormLabel>
                                <Input
                                    size="sm"
                                    type="password"
                                    value={auth.password}
                                    onChange={(e) => {
                                        const newAuth = { ...auth, password: e.target.value };
                                        setAuth(newAuth);
                                        // Save immediately
                                        localStorage.setItem(getServerStorageKey("password"), newAuth.password || "");
                                        window.dispatchEvent(new Event('storage'));
                                        window.dispatchEvent(new Event('auth-updated'));
                                    }}
                                    placeholder="Enter password"
                                    borderColor={!auth.isAuthenticated && (!auth.password || auth.password === "") ? "red.300" : "inherit"}
                                    _hover={{ borderColor: !auth.isAuthenticated && (!auth.password || auth.password === "") ? "red.400" : "inherit" }}
                                    _focus={{ borderColor: !auth.isAuthenticated && (!auth.password || auth.password === "") ? "red.500" : "green.500" }}
                                />
                            </Box>
                            )}
                        </>
                    )}
                </>
            )}

            {/* <Box>
                <HStack spacing={2} justify="space-between">
                    <Text fontSize="xs" color="gray.600">
                        Status: {auth.username ? "Basic auth set" :
                                auth.api_key ? "API Key set" : "No authentication"}
                    </Text>
                    <Button size="xs" variant="ghost" colorScheme="red" onClick={() => {
                        // Clear all auth for current server
                        localStorage.removeItem(getServerStorageKey("api_key"));
                        localStorage.removeItem(getServerStorageKey("username"));
                        localStorage.removeItem(getServerStorageKey("password"));
                        setAuth({
                            api_key: "",
                            username: "",
                            password: "",
                        });
                        window.dispatchEvent(new Event('storage'));
                    }}>
                        Clear
                    </Button>
                </HStack>
            </Box> */}

            {/* Device Flow Modal */}
            <Modal isOpen={isDeviceFlowOpen} onClose={() => { onDeviceFlowClose(); deviceFlowAuth.reset(); }} size="md">
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Authenticate with Nucleus</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        {deviceFlowAuth.isLoading && (
                            <VStack spacing={4} py={4}>
                                <Text>Connecting to Nucleus server...</Text>
                            </VStack>
                        )}
                        
                        {deviceFlowAuth.deviceFlowData && !deviceFlowAuth.authResult && (
                            <VStack spacing={4} py={4} align="stretch">
                                <Text fontSize="sm" color="gray.300">
                                    To authenticate, visit the Nucleus server and enter the code below:
                                </Text>
                                
                                <Box bg="gray.700" p={4} borderRadius="md" textAlign="center">
                                    <Text fontSize="2xl" fontWeight="bold" letterSpacing="0.2em" color="green.400">
                                        {deviceFlowAuth.deviceFlowData.user_code}
                                    </Text>
                                </Box>
                                
                                <VStack spacing={2}>
                                    <Link 
                                        href={(() => {
                                            const uri = deviceFlowAuth.deviceFlowData.verification_uri;
                                            // If verification_uri has a port (e.g., https://server:3180/...), use standard login URL instead
                                            if (uri && /:\d+/.test(uri)) {
                                                const serverHost = getServerHttpsUrl(backend).replace(/^https?:\/\//, '').split('/')[0];
                                                return `https://${serverHost}/omni/auth/login/device`;
                                            }
                                            return uri || getServerHttpsUrl(backend);
                                        })()} 
                                        isExternal 
                                        color="blue.400"
                                    >
                                        Open Nucleus Login Page <ExternalLinkIcon mx="2px" />
                                    </Link>
                                </VStack>
                                
                                {deviceFlowAuth.isPolling && (
                                    <HStack justify="center" spacing={2}>
                                        <Box 
                                            as="span" 
                                            w={2} 
                                            h={2} 
                                            bg="green.400" 
                                            borderRadius="full"
                                            animation="pulse 1.5s ease-in-out infinite"
                                        />
                                        <Text fontSize="sm" color="gray.400">
                                            Waiting for you to enter the code...
                                        </Text>
                                    </HStack>
                                )}
                                
                                <Text fontSize="xs" color="gray.500" textAlign="center">
                                    Code expires in {Math.floor((deviceFlowAuth.deviceFlowData.expires_in || 900) / 60)} minutes
                                </Text>
                            </VStack>
                        )}
                        
                        {deviceFlowAuth.error && (
                            <VStack spacing={4} py={4}>
                                <Text color="red.400">{deviceFlowAuth.error}</Text>
                                <Button size="sm" onClick={handleStartDeviceFlow}>
                                    Try Again
                                </Button>
                            </VStack>
                        )}
                    </ModalBody>
                    <ModalFooter>
                        <Button variant="ghost" onClick={() => { onDeviceFlowClose(); deviceFlowAuth.reset(); }}>
                            Cancel
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </VStack>
    );
};

// Header Icons Component
const HeaderIcons = () => {
    // Server selection state
    const [selectedServer, setSelectedServer] = useState(() => {
        // Check URL for server parameter first
        const urlParams = new URLSearchParams(window.location.search);
        const serverParam = urlParams.get('server');
        
        // If server is in URL and exists in mapping, use it
        if (serverParam && SERVER_MAPPING[serverParam]) {
            return serverParam;
        }
        
        // Otherwise, if we have servers in the mapping, select the first one
        const servers = Object.keys(SERVER_MAPPING);
        const defaultServer = servers.length > 0 ? servers[0] : "";
        console.log("defaultServer", defaultServer);
        return defaultServer;
    });

    // Helper function to get server-specific storage key
    const getServerStorageKey = (key) => {
        if (!selectedServer) return key;
        return `${selectedServer}_${key}`;
    };

    const [auth, setAuth] = useState({
        api_key: localStorage.getItem(getServerStorageKey("api_key")) || "",
        username: localStorage.getItem(getServerStorageKey("username")) || "",
        password: localStorage.getItem(getServerStorageKey("password")) || "",
    });
    const [apiUrl, setApiUrl] = useState(() => {
        // Use server-specific apiUrl if available, otherwise fall back to default
        return selectedServer && SERVER_MAPPING[selectedServer]?.apiUrl || defaultApiUrl;
    });
    const [embeddingConfig, setEmbeddingConfig] = useState(() => {
        return selectedServer && SERVER_MAPPING[selectedServer]?.embedding_config || defaultEmbeddingConfig;
    });

    // Handle server change
    const handleServerChange = (serverName) => {
        setSelectedServer(serverName);
        
        // Get the new embedding config from the server configuration
        const newEmbeddingConfig = SERVER_MAPPING[serverName]?.embedding_config || defaultEmbeddingConfig;
        setEmbeddingConfig(newEmbeddingConfig);
        
        // // Update apiUrl for the new server
        // setApiUrl(SERVER_MAPPING[serverName]?.apiUrl || defaultApiUrl);
        
        // Load server-specific auth
        const newAuth = {
            api_key: localStorage.getItem(`${serverName}_api_key`) || "",
            username: localStorage.getItem(`${serverName}_username`) || "",
            password: localStorage.getItem(`${serverName}_password`) || "",
        };
        setAuth(newAuth);
        
        // Update URL while preserving existing parameters
        const params = new URLSearchParams(window.location.search);
        const existingParams = {};
        
        
        // Save all existing parameters
        params.forEach((value, key) => {
            existingParams[key] = value;
        });
        
        // Update server parameter
        existingParams.server = serverName;
        
        // Reconstruct URL with all parameters
        const newParams = new URLSearchParams(existingParams);
        const url = new URL(window.location);
        url.search = newParams.toString();
        window.history.replaceState({}, '', url);
                
        // Dispatch a custom event to notify other components about the server change
        window.dispatchEvent(new CustomEvent('server-changed', { 
            detail: { server: serverName, embeddingConfig: newEmbeddingConfig }
        }));        
    };
    
    // Use disclosure for auth popover - open by default when no auth is set initially
    const initialHasAuth = auth.api_key || (auth.username && auth.password);
    const { isOpen: isAuthOpen, onOpen: onAuthOpen, onClose: onAuthClose, onToggle: onAuthToggle } = useDisclosure({ 
        defaultIsOpen: !initialHasAuth 
    });
        
    const [plugins, setPlugins] = useState({ active: [], inactive: [] });
    const [backend, setBackend] = useState(null);
    const [loading, setLoading] = useState(false);

    // Listen for storage changes to update auth state
    useEffect(() => {
        const handleStorageChange = () => {
            const newAuth = {
                api_key: localStorage.getItem(getServerStorageKey("api_key")) || "",
                username: localStorage.getItem(getServerStorageKey("username")) || "",
                password: localStorage.getItem(getServerStorageKey("password")) || "",
            };
            setAuth(newAuth);
        };

        const handleAuthUpdate = () => {
            handleStorageChange();
        };

        window.addEventListener('storage', handleStorageChange);
        window.addEventListener('auth-updated', handleAuthUpdate);
        
        return () => {
            window.removeEventListener('storage', handleStorageChange);
            window.removeEventListener('auth-updated', handleAuthUpdate);
        };
    }, [onAuthClose, selectedServer]);


    const getHeaders = () => {
        const headers = { "Content-Type": "application/json" };

        // Add storage backend header if a server is selected
        if (selectedServer) {
            headers["x-usdsearch-storage-backend"] = selectedServer;
        }

        // Get server-specific auth if available
        const serverAuth = {
            api_key: localStorage.getItem(getServerStorageKey("api_key")) || "",
            username: localStorage.getItem(getServerStorageKey("username")) || "",
            password: localStorage.getItem(getServerStorageKey("password")) || "",
        };

        if (serverAuth.username && serverAuth.username.trim() !== "") {
            console.log("Using basic auth with username:", serverAuth.username);
            headers["Authorization"] = `Basic ${btoa(`${serverAuth.username}:${serverAuth.password || ""}`)}`;
        } else if (serverAuth.api_key) {
            console.log("Using API key auth");
            headers["x-api-key"] = serverAuth.api_key;
        } else {
            console.log("No authentication configured");
        }
        
        console.log("Final headers:", headers);
        return headers;
    };

    const fetchPluginsInfo = async (selectedServerOverride = null) => {
        try {
            setLoading(true);
            const headers = getHeaders();
            const fullUrl = defaultApiUrl ? `${defaultApiUrl}/info/plugins` : `/info/plugins`;

            const response = await fetch(fullUrl, { 
                method: 'GET',
                headers: headers 
            });

            if (response.ok) {
                const data = await response.json();

                // Handle different response formats
                if (Array.isArray(data)) {
                    // If data is just an array of plugin names
                    setPlugins({ active: data, inactive: [] });
                } else if (data.active || data.inactive) {
                    // If data has active/inactive structure
                    setPlugins(data);
                } else {
                    // If data is an object with plugin info
                    setPlugins({ active: Object.keys(data), inactive: [] });
                }
            } else {
                const errorText = await response.text();
                console.error("Failed to fetch plugins:", response.status, response.statusText, errorText);
                
                // Try without auth headers if auth failed
                if (response.status === 401 || response.status === 403) {
                    // Keep the storage backend header but remove auth headers
                    const noAuthHeaders = { 
                        "Content-Type": "application/json",
                        ...(selectedServer && { "x-usdsearch-storage-backend": selectedServerOverride ? selectedServerOverride:selectedServer })
                    };
                    const noAuthResponse = await fetch(fullUrl, {
                        method: 'GET',
                        headers: noAuthHeaders
                    });
                    if (noAuthResponse.ok) {
                        const data = await noAuthResponse.json();

                        // Handle different response formats
                        if (Array.isArray(data)) {
                            setPlugins({ active: data, inactive: [] });
                        } else if (data.active || data.inactive) {
                            setPlugins(data);
                        } else {
                            setPlugins({ active: Object.keys(data), inactive: [] });
                        }
                    }
                }
            }
        } catch (error) {
            console.error("Error fetching plugins info:", error);
        } finally {
            setLoading(false);
        }
    };

    const fetchBackendInfo = async (selectedServerOverride = null) => {
        try {
            const headers = getHeaders();
            const fullUrl = defaultApiUrl ? `${defaultApiUrl}/info/backend/storage` : `/info/backend/storage`;

            const response = await fetch(fullUrl, { 
                method: 'GET',
                headers: headers 
            });
            console.log("Backend response:", response.status, response.statusText);
            
            if (response.ok) {
                const data = await response.json();
                console.log("Backend data received:", data);
                
                // Parse the backends structure
                if (data.backends && Object.keys(data.backends).length > 0) {
                    const backendInfo = Object.entries(data.backends).map(([url, info]) => ({
                        url,
                        type: info.storage_backend_type,
                        baseUrl: info.base_url
                    }));
                    setBackend(backendInfo);
                } else {
                    setBackend(null);
                }
            } else {
                const errorText = await response.text();
                console.error("Failed to fetch backend:", response.status, response.statusText, errorText);
                
                // Try without auth headers if auth failed
                if (response.status === 401 || response.status === 403) {
                    console.log("Retrying backend without auth headers...");
                    // Keep the storage backend header but remove auth headers
                    const noAuthHeaders = { 
                        "Content-Type": "application/json",
                        ...(selectedServer && { "x-usdsearch-storage-backend": selectedServerOverride ? selectedServerOverride:selectedServer })
                    };
                    const noAuthResponse = await fetch(fullUrl, {
                        method: 'GET',
                        headers: noAuthHeaders
                    });
                    if (noAuthResponse.ok) {
                        const data = await noAuthResponse.json();
                        console.log("Backend data (no auth):", data);
                        
                        if (data.backends && Object.keys(data.backends).length > 0) {
                            const backendInfo = Object.entries(data.backends).map(([url, info]) => ({
                                url,
                                type: info.storage_backend_type,
                                baseUrl: info.base_url
                            }));
                            setBackend(backendInfo);
                        } else {
                            setBackend(null);
                        }
                    }
                }
            }
        } catch (error) {
            console.error("Error fetching backend info:", error);
        }
    };

    useEffect(() => {
        console.log("HeaderIcons mounted, auth state:", auth);
        console.log("API URL:", apiUrl);
        console.log("Embedding Config:", embeddingConfig);
        fetchPluginsInfo();
        fetchBackendInfo();
        
        // Dispatch initial server configuration so other components get the correct initial state
        if (selectedServer && SERVER_MAPPING[selectedServer]) {
            const initialEmbeddingConfig = SERVER_MAPPING[selectedServer]?.embedding_config || defaultEmbeddingConfig;
            console.log("Dispatching initial server config:", selectedServer, initialEmbeddingConfig);
            window.dispatchEvent(new CustomEvent('server-changed', { 
                detail: { server: selectedServer, embeddingConfig: initialEmbeddingConfig }
            }));
        }
    }, []);
    
    return (
        <HStack spacing={4}>
            {Object.keys(SERVER_MAPPING).length > 0 && (
                <Popover defaultIsOpen={true}>
                    <PopoverTrigger>
                        <HStack 
                            spacing={2} 
                            bg="#76B900"
                            px={3}
                            py={1.5}
                            borderRadius="md"
                            cursor="pointer"
                            _hover={{ bg: "#86C900" }}
                            minW="100px"
                        >
                            <Text 
                                color="black" 
                                fontSize="sm" 
                                fontWeight="medium"
                                noOfLines={1}
                            >
                                {SERVER_MAPPING[selectedServer]?.name || "Select Server"}
                            </Text>
                            <IconButton
                                size="xs"
                                variant="unstyled"
                                icon={<ChevronDownIcon color="black" />}
                                aria-label="Select server"
                                height="auto"
                                minW="auto"
                                display="inline-flex"
                            />
                        </HStack>
                    </PopoverTrigger>
                    <PopoverContent width="400px">
                        <PopoverArrow />
                        <PopoverCloseButton />
                        <PopoverHeader>Server Configuration</PopoverHeader>
                        <PopoverBody>
                            <VStack spacing={4} align="stretch">
                                <Box>
                                    <Text fontWeight="bold" mb={2}>Server Selection</Text>
                                    <Select
                                        size="sm"
                                        value={selectedServer}
                                        onChange={(e) => handleServerChange(e.target.value)}
                                        bg="gray.700"
                                        color="white"
                                        borderColor="gray.600"
                                        _hover={{ borderColor: "green.500" }}
                                        _focus={{ borderColor: "green.500", boxShadow: "0 0 0 1px var(--chakra-colors-green-500)" }}
                                    >
                                        {Object.entries(SERVER_MAPPING).map(([key, config]) => (
                                            <option key={key} value={key}>{config.name}</option>
                                        ))}
                                    </Select>
                                </Box>
                                
                                <Divider />
                                
                                <Box>
                                    <HStack justify="space-between" mb={2}>
                                        <Text fontWeight="bold">Authentication</Text>
                                        <HStack spacing={1}>
                                            <Text fontSize="sm" color="gray.500">Status:</Text>
                                            <Text fontSize="sm" color={auth.api_key || (auth.username && auth.password) ? "green.500" : "red.500"}>
                                                {auth.api_key || (auth.username && auth.password) ? "Authenticated" : "Not Authenticated"}
                                            </Text>
                                            {auth.api_key || (auth.username && auth.password) ? <LockIcon color="green.500" /> : <UnlockIcon color="red.500" />}
                                        </HStack>
                                    </HStack>
                                    <AuthForm auth={auth} setAuth={setAuth} getServerStorageKey={getServerStorageKey} />
                                </Box>
                            </VStack>
                        </PopoverBody>
                    </PopoverContent>
                </Popover>
            )}
            {!Object.keys(SERVER_MAPPING).length > 0 && (
                <Popover isOpen={isAuthOpen} onClose={onAuthClose}>
                    <PopoverTrigger>
                        <IconButton
                            size="sm"
                            icon={auth.api_key || auth.username ? <LockIcon /> : <UnlockIcon />}
                            aria-label="Authentication status"
                            bg="rgba(0,0,0,0.1)"
                            color="black"
                            _hover={{ bg: "rgba(0,0,0,0.2)" }}
                            onClick={onAuthToggle}
                        />
                    </PopoverTrigger>
                    <PopoverContent>
                        <PopoverArrow />
                        <PopoverCloseButton />
                        <PopoverHeader>Authentication Status</PopoverHeader>
                        <PopoverBody>
                            <AuthForm auth={auth} setAuth={setAuth} getServerStorageKey={getServerStorageKey} />
                        </PopoverBody>
                    </PopoverContent>
                </Popover>
            )}
            <Popover>
                <PopoverTrigger>
                    <IconButton
                        size="sm"
                        icon={<InfoIcon />}
                        aria-label="Instance information"
                        bg="rgba(0,0,0,0.1)"
                        color="black"
                        _hover={{ bg: "rgba(0,0,0,0.2)" }}
                        onClick={() => { fetchPluginsInfo(); fetchBackendInfo(); }}
                    />
                </PopoverTrigger>
                <PopoverContent width="600px">
                    <PopoverArrow />
                    <PopoverCloseButton />
                    <PopoverHeader>
                        <HStack justify="space-between">
                            <Text>Instance Information</Text>
                            <Button size="xs" onClick={() => { fetchPluginsInfo(); fetchBackendInfo(); }}>
                                Refresh
                            </Button>
                        </HStack>
                    </PopoverHeader>
                    <PopoverBody>
                        <VStack spacing={4} align="stretch">
                            <Box>
                                <Text fontWeight="bold" mb={2} color="white">Storage Backends</Text>
                                {loading ? (
                                    <Text fontSize="sm" color="gray.300">Loading...</Text>
                                ) : backend && Array.isArray(backend) ? (
                                    <VStack align="start" spacing={2}>
                                        {backend.map((backendItem, index) => (
                                            <Box key={index} p={2} bg="gray.700" borderRadius="md" w="100%">
                                                <Text fontSize="sm" color="white" fontWeight="medium">
                                                    {backendItem.type.toUpperCase()} Storage
                                                </Text>
                                                <Text fontSize="xs" color="gray.300" mt={1}>
                                                    {backendItem.url}
                                                </Text>
                                                {backendItem.baseUrl !== backendItem.url && (
                                                    <Text fontSize="xs" color="gray.400" mt={1}>
                                                        Base: {backendItem.baseUrl}
                                                    </Text>
                                                )}
                                            </Box>
                                        ))}
                                    </VStack>
                                ) : (
                                    <VStack align="start" spacing={1}>
                                        <Text fontSize="sm" color="gray.300">No backend information available</Text>
                                        <Button size="xs" onClick={fetchBackendInfo}>Retry</Button>
                                    </VStack>
                                )}
                            </Box>
                            <Divider />
                            <Box>
                                <Text fontWeight="bold" mb={2} color="white">Supported Plugins</Text>
                                {loading ? (
                                    <Text fontSize="sm" color="gray.300">Loading...</Text>
                                ) : plugins && (plugins.active?.length > 0 || plugins.inactive?.length > 0) ? (
                                    <Box maxH="300px" overflowY="auto">
                                        {plugins.active && plugins.active.length > 0 && (
                                            <Box mb={3}>
                                                <Text fontWeight="semibold" color="green.400" mb={2}>Active Plugins ({plugins.active.length})</Text>
                                                {plugins.active.map((plugin, index) => (
                                                    <Box key={index} mb={2}>
                                                        <Text fontSize="sm" color="white" fontWeight="medium">
                                                            {plugin.name || plugin}
                                                        </Text>
                                                        {plugin.description && (
                                                            <Text fontSize="xs" color="gray.300" ml={2} mt={1}>
                                                                {plugin.description}
                                                            </Text>
                                                        )}
                                                    </Box>
                                                ))}
                                            </Box>
                                        )}
                                        {plugins.inactive && plugins.inactive.length > 0 && (
                                            <Box mb={3}>
                                                <Text fontWeight="semibold" color="gray.400" mb={2}>Inactive Plugins ({plugins.inactive.length})</Text>
                                                {plugins.inactive.map((plugin, index) => (
                                                    <Box key={index} mb={2}>
                                                        <Text fontSize="sm" color="gray.200" fontWeight="medium">
                                                            {plugin.name || plugin}
                                                        </Text>
                                                        {plugin.description && (
                                                            <Text fontSize="xs" color="gray.300" ml={2} mt={1}>
                                                                {plugin.description}
                                                            </Text>
                                                        )}
                                                    </Box>
                                                ))}
                                            </Box>
                                        )}
                                    </Box>
                                ) : (
                                    <VStack align="start" spacing={1}>
                                        <Text fontSize="sm" color="gray.300">No plugins information available</Text>
                                        <Button size="xs" onClick={fetchPluginsInfo}>Retry</Button>
                                    </VStack>
                                )}
                            </Box>
                        </VStack>
                    </PopoverBody>
                </PopoverContent>
            </Popover>
        </HStack>
    );
};

// App wrapper to initialize persistent cache
const App = () => {
    useEffect(() => {
        // Initialize persistent image cache on app startup
        persistentCache.init().then(supported => {
            console.log(`Persistent image cache ${supported ? 'initialized' : 'not supported'}`);
        }).catch(err => {
            console.warn('Failed to initialize persistent image cache:', err);
        });
    }, []);

    return (
        <ChakraProvider theme={theme}>
            <Box w="100%" h="90px" backgroundColor="#76B900">
                <Flex h="100%" alignItems="center" flexDir="row" justify="space-between" px={4}>
                    <Flex alignItems="center">
                        <Image src={logo} alt="NVIDIA" h="72px"/>
                        <Flex alignItems={"flex-end"}>
                            <Heading lineHeight={"0.7"} ml="1rem" fontSize="4xl" color="black">USD SEARCH EXPLORER</Heading>
                            <Heading lineHeight={"0.7"} fontSize={"small"} color="black" ml={"0.3rem"}>v{process.env.REACT_APP_GIT_SHA ? process.env.REACT_APP_GIT_SHA : " UNKNOWN"}</Heading>
                        </Flex>
                    </Flex>
                    <HeaderIcons handleSearch={() => window.dispatchEvent(new Event('trigger-search'))} />
                </Flex>
            </Box>
            <ColorModeScript initialColorMode={theme.config.initialColorMode}/>
            <SearchApp/>
        </ChakraProvider>
    );
};

const container = document.getElementById('root');
const root = ReactDOMClient.createRoot(container);
root.render(
  <React.StrictMode>
      <App/>
  </React.StrictMode>
);

