from genderbias.detector import Detector, Flag, Issue, Report
import os

"""
Letters for women are less likely to include agentic words.

"Prior research found that agentic terms were more frequent in letters for men
and communal terms were more frequent in letters for women. Agentic behaviors
at work include speaking assertively, influencing others, and initiating tasks.
Corresponding communal behaviors include being concerned with the welfare of
others (i.e., descriptions of kindness, sympathy, sensitivity, and nurturance),
helping others, accepting others’ direction, and maintaining relationships."
(Madera et al. 2009)

Goal: Combine this with communal detector.
"""
_dir = os.path.dirname(__file__)
AGENTIC_WORDS = [word.strip() for word in open(_dir + "/agentic.wordlist", 'r').readlines()]
COMMUNAL_WORDS = [word.strip() for word in open(_dir + "/communal.wordlist", 'r').readlines()]

class AgenticDetector(Detector):
    def get_report(self, doc):
        agentic_report = Report("agentic")
        words_with_indices = doc.words_with_indices()

        found_communal = False
        found_agentic = False
        for word, start, stop in words_with_indices:

            if word.lower() in AGENTIC_WORDS:
                found_agentic = True
                agentic_report.add_flag(
                    Flag(start, stop, Issue("agenticWord",
                                            " '{word}' is an agentic word.".format(
                                                word=word), bias=Issue.positive_result)))
            if word.lower() in COMMUNAL_WORDS:
                found_communal = True
                agentic_report.add_flag(
                    Flag(start, stop, Issue(
                        "communalWord",
                        " '{word}' is a communal word.".format(
                            word=word),
                        "Communal words should be replaced with agentic words or removed."
                    ))
                )

        if found_agentic and found_communal:
            agentic_report.set_summary("Found some agentic words used to describe the subject as well as communal words. Consider the necessity of the communal words. Communal terms such as describing how the subject cares for the welfare of others is typically associated with females (example: 'nice', 'understanding', 'compassionate', etc.).")
        elif found_agentic:
            agentic_report.set_summary("There were some agentic words, but no communal words. This is okay.")
        elif found_communal:
            agentic_report.set_summary("There were no agentic words, but did contain communal words. Communal words are strongly gendered and appear more in female letters. They deal with talking about the subject in relation to others (example: 'nice', 'understanding', 'compassionate', etc.) as opposed to agentic words which deal with ability (example: 'ambitious', 'confident', 'able', etc.).")

        return agentic_report
