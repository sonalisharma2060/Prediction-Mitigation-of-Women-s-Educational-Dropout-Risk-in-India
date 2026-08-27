"""
mitigation.py
-------------
Maps a student's risk factors to concrete, actionable mitigation
suggestions.
"""

from typing import List, Dict


def get_mitigation_suggestions(input_dict: Dict) -> List[str]:
    suggestions = []

    if input_dict["early_marriage_risk"] == "Yes":
        suggestions.append(
            "High priority: Engage family counseling and local child-marriage "
            "prevention programs (e.g. under the Prohibition of Child Marriage Act) "
            "to delay marriage until education is complete."
        )

    if input_dict["family_income"] == "Below 1 Lakh":
        suggestions.append(
            "Enroll the student in government scholarship schemes for girls "
            "(e.g. National Scheme for Incentive to Girls for Secondary Education) "
            "to offset the financial burden."
        )

    if input_dict["toilet_facility"] == "No":
        suggestions.append(
            "Advocate for separate, functional toilet facilities at school - "
            "lack of sanitation is a well-documented cause of girls dropping out "
            "after puberty."
        )

    if input_dict["distance_to_school_km"] > 3:
        suggestions.append(
            "Explore safe transport options (school bus/cycle scheme) or "
            "hostel facilities, since long commutes disproportionately affect "
            "girls' school continuation due to safety concerns."
        )

    if input_dict["mother_education"] in ("Illiterate", "Primary"):
        suggestions.append(
            "Involve the mother in adult literacy or awareness programs - "
            "maternal education level strongly correlates with daughters' "
            "school retention."
        )

    if input_dict["attendance_percentage"] < 70:
        suggestions.append(
            "Set up regular attendance monitoring with early alerts to "
            "teachers/parents when attendance drops, to intervene before "
            "the student disengages completely."
        )

    if input_dict["academic_performance"] < 50:
        suggestions.append(
            "Arrange peer tutoring or remedial classes to rebuild academic "
            "confidence - poor performance is often a precursor to dropout."
        )

    if input_dict["internet_access"] == "No":
        suggestions.append(
            "Provide access to community digital learning centers to bridge "
            "the resource gap, especially for supplementary learning."
        )

    if input_dict["scholarship"] == "No" and input_dict["family_income"] != "Above 5 Lakh":
        suggestions.append(
            "Check eligibility for state/central scholarship schemes - many "
            "eligible families are unaware these exist."
        )

    if not suggestions:
        suggestions.append(
            "No major risk factors detected. Continue regular monitoring of "
            "attendance and academic performance as a preventive measure."
        )

    return suggestions
