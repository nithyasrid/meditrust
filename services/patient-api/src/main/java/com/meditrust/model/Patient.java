package com.meditrust.model;

public record Patient(
        String patientId,
        String fullName,
        String dateOfBirth,
        String gender,
        String phone,
        String insuranceId,
        String admissionDate
) {}
