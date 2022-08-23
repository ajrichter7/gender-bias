import os
import re

from ..detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)
MALE_WORDS = [
    word.strip() for word in open(_dir + "/Malewords.wordlist", "r").readlines()
]


class MaleDetector(Detector):
    """
    Detect words that are more commonly used to recruit men rather than women.

    """

    def get_report(self, doc):
        male_report = Report("Terms biased towards men:")
        words_with_indices = doc.words_with_indices()
        # print(words_with_indices)

        found = False
        for word, start, stop in words_with_indices:
            if word.lower() in MALE_WORDS:
                found = True 
                female_report.add_flag(
                    Flag(
                        start,
                        stop,
                        Issue(
                            "Male Gendered Word",
                            f"The word '{word}' is male gendered.",
                            "Consider if this is an important phrasing or descriptor to include.",
                            bias=Issue.negative_result,
                        ),
                    )
                )
        if found:
            male_report.set_summary(
                "Depending on context, these words may be biased towards recruiting men"
            )
        else:
            male_report.set_summary("There are no biased terms.")
            print(male_report.pprint())
        return male_report
