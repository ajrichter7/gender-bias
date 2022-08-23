import os
import re

from ..detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)
FEMALE_WORDS = [
    word.strip() for word in open(_dir + "/Femalewords.wordlist", "r").readlines()
]


class FemaleDetector(Detector):
    """
    A detector for words that tend to be used more frequently for recruiting
    women than for recruiting men.

    """

    def get_report(self, doc):
        female_report = Report("\nTerms biased towards women")
        words_with_indices = doc.words_with_indices()

        found = False
        for word, start, stop in words_with_indices:
            if word.lower() in FEMALE_WORDS:
                found = True
                female_report.add_flag(
                    Flag(
                        start,
                        stop,
                        Issue(
                            "Female Gendered Word",
                            f"The word '{word}' is female gendered.",
                            "Consider if this is an important phrasing or descriptor to include",
                            bias=Issue.negative_result,
                        ),
                    )
                )

        if found:
            female_report.set_summary(
                "Depending on context, these words may be biased towards recruiting women"
            )
        else:
            female_report.set_summary("There are no biased terms.")
            print(female_report.pprint())
        return female_report
