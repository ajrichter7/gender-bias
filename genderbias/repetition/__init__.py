import os
from ..document import Document
from ..detector import Detector, Flag, Issue, Report

_dir = os.path.dirname(__file__)
STANDOUT_WORDS = [
    word.strip() for word in open(_dir + "/standout.wordlist", "r").readlines()
]
class RepetitionDetector(Detector):
    """
    This detector checks for repetition of standout words. Word list from Trix and Psenka 2003.
    """

    def get_report(self, doc):
        """
        I think this does it correctly. Originally I was counting the prevalence by checking all the words in the doc, but I think Trix and Psenka are just saying to count the number of repeated standout words in a single letter? Need verification. 
        """
        repetiton_report = Report("Repetition")

        token_indices = doc.words_with_indices()
        found_repetition = False
        num = 0
        for word, start, stop in token_indices:
            if word.lower() in STANDOUT_WORDS and found_repetition:
                num +=1
                repetiton_report.add_flag(
                    Flag(start, stop, Issue("Repetition",
                                            "There is a repetition in standout words, which is good.",
                                            bias=Issue.positive_result)))
            if word.lower() in STANDOUT_WORDS:
                num +=1
                found_repetition = True
        if found_repetition:
            repetiton_report.set_summary("Standout words are being repeated. There are {num} standout words in this letter of recommendation. According to Trix and Psenka (2003), letters of recommendation for women contain 1.5 standout words while letters of recommendation for men contain 2.0. How do you compare?".format(num=num))
        else:
            repetiton_report.set_summary("This letter of recommendation strongly needs more standout words.")
        return repetiton_report
