/**
 * SPDX-FileCopyrightText: Copyright (c) 2024-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

import React, { useState, useEffect } from "react";
import {
  Box,
  VStack,
  HStack,
  Text,
  Switch,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Divider,
  Badge,
  Tooltip,
  IconButton,
  Select,
  FormControl,
  FormLabel,
  Slider,
  SliderTrack,
  SliderFilledTrack,
  SliderThumb,
  Collapse,
  useDisclosure,
} from "@chakra-ui/react";
import { InfoIcon, SettingsIcon, ChevronDownIcon, ChevronUpIcon } from "@chakra-ui/icons";

// Field display name mapping
const getFieldDisplayName = (fieldName) => {
  const fieldNames = {
    "name": "Name",
    "usd_properties.value": "USD Properties Value",
    "usd_properties.key": "USD Properties Key", 
    "path": "Path",
    "path.tree": "Path Tree",
    "path.tree_reverse": "Path Tree Reverse",
    "__VISION_METADATA_FIELDS__": "Vision Metadata (All Fields)"
  };
  return fieldNames[fieldName] || fieldName;
};

const DEFAULT_HYBRID_CONFIG = {
  rrf_config: {
    rank_constant: 60,
    // window_size: null,
    query_rank_constants: {}
  },
  vector_text_expansion: {
    enabled: false
  },
  hybrid_text: {
    enabled: true,
    weight: 1.2,
    fields: [
      { field: "name", nested: false, enabled: true, weight: 2.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "name.simple", nested: false, enabled: true, weight: 2.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "name.standard", nested: false, enabled: true, weight: 2.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "usd_properties.value", nested: true, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "usd_properties.key", nested: true, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "path", nested: false, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "path.tree", nested: false, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "path.tree_reverse", nested: false, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
      { field: "__VISION_METADATA_FIELDS__", nested: false, enabled: true, weight: 1.0, match_type: "fuzzy", fuzzy_max_expansions: 1, wildcard: true },
    ],
    cross_field_operator: "or"
  },
  vector_fields: {
    "clip-embedding.embedding": {
      enabled: true,
      weight: 1.0,
      field_name: "clip-embedding.embedding",
      dimension: 1024,
      // model_name: null
    }
  }
};

const HybridSearchConfig = ({ value = DEFAULT_HYBRID_CONFIG, onChange, isCollapsed = true }) => {
  const [config, setConfig] = useState(value);
  const { isOpen, onToggle } = useDisclosure({ defaultIsOpen: !isCollapsed });

  // Sync internal state with prop value when it changes
  useEffect(() => {
    setConfig(value);
  }, [value]);

  const updateConfig = (newConfig) => {
    setConfig(newConfig);
    onChange?.(newConfig);
  };

  const updateHybridText = (field, fieldValue) => {
    const newConfig = {
      ...config,
      hybrid_text: {
        ...config.hybrid_text,
        [field]: fieldValue
      }
    };
    updateConfig(newConfig);
  };

  const updateHybridTextField = (fieldIndex, field, fieldValue) => {
    const newFields = [...config.hybrid_text.fields];
    newFields[fieldIndex] = {
      ...newFields[fieldIndex],
      [field]: fieldValue
    };
    
    // If setting match_type to "exact", remove fuzzy_max_expansions
    if (field === 'match_type' && fieldValue === 'exact') {
      delete newFields[fieldIndex].fuzzy_max_expansions;
    }
    // If setting match_type to "fuzzy", ensure fuzzy_max_expansions exists
    else if (field === 'match_type' && fieldValue === 'fuzzy') {
      newFields[fieldIndex].fuzzy_max_expansions = newFields[fieldIndex].fuzzy_max_expansions || 1;
    }
    
    const newConfig = {
      ...config,
      hybrid_text: {
        ...config.hybrid_text,
        fields: newFields
      }
    };
    updateConfig(newConfig);
  };

  const updateVectorField = (fieldName, field, fieldValue) => {
    const newConfig = {
      ...config,
      vector_fields: {
        ...config.vector_fields,
        [fieldName]: {
          ...config.vector_fields[fieldName],
          [field]: fieldValue
        }
      }
    };
    updateConfig(newConfig);
  };

  const updateRRFConfig = (field, fieldValue) => {
    const newConfig = {
      ...config,
      rrf_config: {
        ...config.rrf_config,
        [field]: fieldValue
      }
    };
    updateConfig(newConfig);
  };

  return (
    <Box 
      bg="gray.800" 
      pt={0}
      px={4}
      pb={0}
      borderRadius="md" 
      border="1px solid"
      borderColor="gray.600"
    >
      <HStack justify="space-between" mb={4} cursor="pointer" onClick={onToggle} opacity={0.8}>
        <HStack>
          <SettingsIcon color="gray.400" />
          <Text fontSize="md" fontWeight="bold" color="gray.300">
            Advanced Hybrid Search Configuration
          </Text>
          <Badge colorScheme="gray" size="sm">
            {config.hybrid_text.enabled ? 'Text' : ''}
            {config.hybrid_text.enabled && Object.values(config.vector_fields).some(v => v.enabled) ? ' + ' : ''}
            {Object.values(config.vector_fields).some(v => v.enabled) ? 'Vector' : ''}
          </Badge>
        </HStack>
        <IconButton
          size="sm"
          variant="ghost"
          icon={isOpen ? <ChevronUpIcon /> : <ChevronDownIcon />}
          onClick={onToggle}
          aria-label="Toggle configuration"
        />
      </HStack>

      <Collapse in={isOpen} animateOpacity>

      <Accordion allowMultiple defaultIndex={[0]}>
        {/* Hybrid Text Configuration */}
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <HStack>
                <Text fontWeight="semibold">Text Search Fields</Text>
                <Switch
                  isChecked={config.hybrid_text.enabled}
                  onChange={(e) => updateHybridText('enabled', e.target.checked)}
                  colorScheme="green"
                />
              </HStack>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <VStack spacing={4} align="stretch">
              <FormControl>
                <FormLabel fontSize="sm">Text Search Weight</FormLabel>
                <HStack>
                  <Slider
                    value={config.hybrid_text.weight}
                    onChange={(value) => updateHybridText('weight', value)}
                    min={0}
                    max={10}
                    step={0.1}
                    flex={1}
                    colorScheme="green"
                  >
                    <SliderTrack>
                      <SliderFilledTrack />
                    </SliderTrack>
                    <SliderThumb />
                  </Slider>
                  <Text fontSize="sm" w="40px">
                    {config.hybrid_text.weight.toFixed(1)}
                  </Text>
                </HStack>
              </FormControl>

              <Divider />

              <FormControl>
                <FormLabel fontSize="sm">Cross-Field Operator</FormLabel>
                <Select
                  size="sm"
                  value={config.hybrid_text.cross_field_operator || "or"}
                  onChange={(e) => updateHybridText('cross_field_operator', e.target.value)}
                >
                  <option value="or">OR - Match any field</option>
                  <option value="and">AND - Match all fields</option>
                </Select>
              </FormControl>

              <Divider />

              <Text fontSize="sm" fontWeight="semibold">Search Fields:</Text>
              {config.hybrid_text.fields.map((field, index) => (
                <Box key={index} p={3} bg="gray.700" borderRadius="md">
                  <HStack justify="space-between" mb={2}>
                    <HStack>
                      <Text fontSize="sm" fontWeight="medium">
                        {getFieldDisplayName(field.field)}
                      </Text>
                      {field.nested && (
                        <Badge size="sm" colorScheme="blue">Nested</Badge>
                      )}
                    </HStack>
                    <Switch
                      size="sm"
                      isChecked={field.enabled}
                      onChange={(e) => updateHybridTextField(index, 'enabled', e.target.checked)}
                      colorScheme="green"
                    />
                  </HStack>
                  {field.enabled && (
                    <VStack spacing={2} align="stretch">
                      <HStack>
                        <Text fontSize="xs" color="gray.300">Weight:</Text>
                        <Slider
                          value={field.weight}
                          onChange={(value) => updateHybridTextField(index, 'weight', value)}
                          min={0}
                          max={5}
                          step={0.1}
                          flex={1}
                          size="sm"
                          colorScheme="green"
                        >
                          <SliderTrack>
                            <SliderFilledTrack />
                          </SliderTrack>
                          <SliderThumb />
                        </Slider>
                        <Text fontSize="xs" w="30px">
                          {field.weight.toFixed(1)}
                        </Text>
                      </HStack>
                      <HStack justify="space-between">
                        <HStack spacing={1}>
                          <Text fontSize="xs" color="gray.300">Match Type:</Text>
                          <Tooltip label="Exact matches require perfect spelling, fuzzy matches allow character differences and are more flexible">
                            <InfoIcon boxSize={3} color="gray.400" />
                          </Tooltip>
                        </HStack>
                        <Switch
                          size="sm"
                          isChecked={field.match_type === "fuzzy"}
                          onChange={(e) => updateHybridTextField(index, 'match_type', e.target.checked ? "fuzzy" : "exact")}
                          colorScheme="orange"
                        />
                        <Text fontSize="xs" color="gray.300">
                          {field.match_type === "fuzzy" ? "Fuzzy" : "Exact"}
                        </Text>
                      </HStack>
                      {field.match_type === "fuzzy" && (
                        <HStack>
                          <HStack spacing={1}>
                            <Text fontSize="xs" color="gray.300">Fuzziness:</Text>
                            <Tooltip label="0 = Exact match only, 1 = Allow 1 character difference, 2 = Allow 2 character differences, etc. Higher values make search more flexible but less precise.">
                              <InfoIcon boxSize={3} color="gray.400" />
                            </Tooltip>
                          </HStack>
                          <Slider
                            value={field.fuzzy_max_expansions !== undefined ? field.fuzzy_max_expansions : 1}
                            onChange={(value) => updateHybridTextField(index, 'fuzzy_max_expansions', value)}
                            min={0}
                            max={5}
                            step={1}
                            flex={1}
                            size="sm"
                            colorScheme="blue"
                          >
                            <SliderTrack>
                              <SliderFilledTrack />
                            </SliderTrack>
                            <SliderThumb />
                          </Slider>
                          <Text fontSize="xs" w="20px">
                            {field.fuzzy_max_expansions !== undefined ? field.fuzzy_max_expansions : 1}
                          </Text>
                        </HStack>
                      )}
                      <HStack justify="space-between">
                        <HStack spacing={1}>
                          <Text fontSize="xs" color="gray.300">Wildcard Search:</Text>
                          <Tooltip label="Enable wildcard matching with * and ? characters. Allows partial matches like 'car*' to match 'car', 'cars', 'carbon', etc.">
                            <InfoIcon boxSize={3} color="gray.400" />
                          </Tooltip>
                        </HStack>
                        <Switch
                          size="sm"
                          isChecked={field.wildcard !== undefined ? field.wildcard : true}
                          onChange={(e) => updateHybridTextField(index, 'wildcard', e.target.checked)}
                          colorScheme="purple"
                        />
                      </HStack>
                    </VStack>
                  )}
                </Box>
              ))}
            </VStack>
          </AccordionPanel>
        </AccordionItem>

        {/* Vector Text Search Expansion */}
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <HStack>
                <Text fontWeight="semibold">Vector Text Search Expansion</Text>
                <Badge colorScheme="orange" variant="outline">
                  EXPERIMENTAL
                </Badge>
                <Badge colorScheme={config.vector_text_expansion?.enabled ? "green" : "gray"}>
                  {config.vector_text_expansion?.enabled ? "Enabled" : "Disabled"}
                </Badge>
              </HStack>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <VStack spacing={4} align="stretch">
              <HStack justify="space-between">
                <VStack align="start" spacing={1}>
                  <Text fontSize="sm" fontWeight="medium">
                    Enable Vector Text Expansion
                  </Text>
                  <Text fontSize="xs" color="gray.300">
                    Send vector queries for the full text query and each individual word
                  </Text>
                </VStack>
                <Switch
                  isChecked={config.vector_text_expansion?.enabled || false}
                  onChange={(e) => {
                    const newConfig = {
                      ...config,
                      vector_text_expansion: {
                        enabled: e.target.checked
                      }
                    };
                    updateConfig(newConfig);
                  }}
                  colorScheme="green"
                />
              </HStack>
            </VStack>
          </AccordionPanel>
        </AccordionItem>

        {/* Vector Fields Configuration */}
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <HStack>
                <Text fontWeight="semibold">Vector Search Fields</Text>
                <Badge colorScheme="purple">
                  {Object.values(config.vector_fields).filter(v => v.enabled).length} active
                </Badge>
              </HStack>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <VStack spacing={4} align="stretch">
              {Object.entries(config.vector_fields).map(([fieldName, fieldConfig]) => (
                <Box key={fieldName} p={3} bg="gray.700" borderRadius="md">
                  <HStack justify="space-between" mb={2}>
                    <VStack align="start" spacing={0}>
                      <Text fontSize="sm" fontWeight="medium">
                        {fieldName}
                      </Text>
                      <Text fontSize="xs" color="gray.300">
                        Dimension: {fieldConfig.dimension}
                      </Text>
                    </VStack>
                    <Switch
                      size="sm"
                      isChecked={fieldConfig.enabled}
                      onChange={(e) => updateVectorField(fieldName, 'enabled', e.target.checked)}
                      colorScheme="purple"
                    />
                  </HStack>
                  {fieldConfig.enabled && (
                    <HStack>
                      <Text fontSize="xs" color="gray.300">Weight:</Text>
                      <Slider
                        value={fieldConfig.weight}
                        onChange={(value) => updateVectorField(fieldName, 'weight', value)}
                        min={0}
                        max={5}
                        step={0.1}
                        flex={1}
                        size="sm"
                        colorScheme="purple"
                      >
                        <SliderTrack>
                          <SliderFilledTrack />
                        </SliderTrack>
                        <SliderThumb />
                      </Slider>
                      <Text fontSize="xs" w="30px">
                        {fieldConfig.weight.toFixed(1)}
                      </Text>
                    </HStack>
                  )}
                </Box>
              ))}
            </VStack>
          </AccordionPanel>
        </AccordionItem>

        {/* RRF Configuration */}
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <HStack>
                <Text fontWeight="semibold">Ranking Configuration</Text>
                <Tooltip label="Reciprocal Rank Fusion (RRF) combines results from different search methods">
                  <InfoIcon boxSize={3} color="gray.400" />
                </Tooltip>
              </HStack>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <VStack spacing={4} align="stretch">
              <Box p={3} bg="gray.700" borderRadius="md">
                <Text fontSize="sm" fontWeight="semibold" color="blue.300" mb={2}>
                  About Reciprocal Rank Fusion (RRF)
                </Text>
                <Text fontSize="xs" color="gray.300" lineHeight="1.4">
                  RRF combines results from different search methods (text search, vector search) by converting scores to ranks, 
                  then computing a weighted average. Lower ranks get higher fusion scores. The rank constant controls how much 
                  weight to give to lower-ranked results - higher values make the fusion more democratic across all results.
                </Text>
              </Box>
              <FormControl>
                <FormLabel fontSize="sm">
                  Rank Constant
                  <Tooltip label="Higher values give more weight to lower-ranked results">
                    <InfoIcon boxSize={3} color="gray.400" ml={1} />
                  </Tooltip>
                </FormLabel>
                <NumberInput
                  value={config.rrf_config.rank_constant}
                  onChange={(value) => updateRRFConfig('rank_constant', parseInt(value) || 60)}
                  min={1}
                  max={1000}
                  size="sm"
                >
                  <NumberInputField />
                  <NumberInputStepper>
                    <NumberIncrementStepper />
                    <NumberDecrementStepper />
                  </NumberInputStepper>
                </NumberInput>
              </FormControl>
              
              <FormControl>
                <FormLabel fontSize="sm">
                  Window Size
                  <Tooltip label="Number of top results to consider for ranking (leave empty for default (2x page size))">
                    <InfoIcon boxSize={3} color="gray.400" ml={1} />
                  </Tooltip>
                </FormLabel>
                <NumberInput
                  value={config.rrf_config.window_size || ''}
                  onChange={(value) => updateRRFConfig('window_size', value === '' ? null : parseInt(value))}
                  min={1}
                  max={10000}
                  size="sm"
                >
                  <NumberInputField placeholder="default" />
                  <NumberInputStepper>
                    <NumberIncrementStepper />
                    <NumberDecrementStepper />
                  </NumberInputStepper>
                </NumberInput>
              </FormControl>
            </VStack>
          </AccordionPanel>
        </AccordionItem>
      </Accordion>
      </Collapse>
    </Box>
  );
};

export default HybridSearchConfig;
export { DEFAULT_HYBRID_CONFIG };