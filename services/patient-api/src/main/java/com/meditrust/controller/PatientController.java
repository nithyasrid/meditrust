package com.meditrust.controller;

import com.meditrust.model.Patient;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/patients")
public class PatientController {

    private final List<Patient> patients = List.of(
        new Patient("P1001", "Arun Kumar", "1999-05-14", "M", "9876543210", "INS1001", "2026-08-01"),
        new Patient("P1002", "Priya Devi", "1987-11-02", "F", "9876543211", "INS1002", "2026-08-02"),
        new Patient("P1003", "Ravi Kumar", null, "M", "9876543212", "INS1003", "2026-08-03")
    );

    @GetMapping
    public List<Patient> getPatients() {
        return patients;
    }

    @GetMapping("/{id}")
    public Object getPatient(@PathVariable String id) {
        return patients.stream()
            .filter(p -> p.patientId().equalsIgnoreCase(id))
            .findFirst()
            .map(p -> (Object) p)
            .orElse(Map.of("error", "Patient not found", "patientId", id));
    }
}
