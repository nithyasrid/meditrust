package com.meditrust.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class QualityController {

    @GetMapping("/api/quality/summary")
    public Map<String, Object> summary() {
        return Map.of(
            "recordsProcessed", 6,
            "recordsWithIssues", 4,
            "duplicatePatients", 2,
            "missingValues", 3,
            "invalidValues", 1,
            "qualityScore", 33.33,
            "status", "NEEDS_ATTENTION"
        );
    }
}
