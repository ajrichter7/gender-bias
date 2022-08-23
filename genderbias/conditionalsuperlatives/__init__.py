#!/usr/bin/env python3

"""
Check for statements that pertain to effort, rather than accomplishment.

Letters for women are more likely to highlight effort (she is hard-working)
instead of highlighting accomplishments (her research is groundbreaking).

Goal: Develop code that can read text for effort statements. If the text
includes more effort statements, than accomplishment statements; return a
summary that directs the author to add statements related to accomplishment.
"""


import os
import re
from genderbias.detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)


_all_women_forms_regex = "(?:woman|girl|women)"

CONDITIONAL_SUPERLATIVE_REGEXES = [fr"\s(\w+est[^\.]*{_all_women_forms_regex})"]


class ConditionalSuperlativesDetector(Detector):
    """
    This detector checks for conditional superlatives, or superlatives that
    are "hedged" by restricting the population to only women.

    This is a good example of how to detect multi-word phrases.

    """

    def get_report(self, doc):
        """
        Generates a report on the text that checks for curbed superlatives.

        These are phrases like "the best woman for the job" or "best of
        all women" that are clear 'hedged' superlatives.


        Arguments:
            doc (Document): The document to check

        Returns:
            Report

        """
        report = Report("Conditional Superlatives")

        text = doc.text()
        found = False
        for regex in CONDITIONAL_SUPERLATIVE_REGEXES:
            for match in re.finditer(regex, text):
                found = True
                report.add_flag(
                    Flag(
                        match.span()[0],
                        match.span()[1],
                        Issue(
                            "Conditional Superlative",
                            "This phrase appears to hedge a superlative to apply only to women.",
                        ),
                    )
                )
        if found:
            report.set_summary("There are conditional superlatives present. Consider removing them.")
        else:
            report.set_summary("No conditional superlatives found. This is a good indicator in this case.")
            print(report.pprint())

        return report
