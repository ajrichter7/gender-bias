# Understanding Detectors

Various detectors have been implemented with the intent to test for bias in letters of recommendation.

## Description
This project investigates various detectors as a way to determine bias in letters of recommendation. Each detector has been thoughtfully chosen and developed. The reasoning behind the detectors is included along with citations for those curious.

NOTE: I will need to change these links when merging because they link to forked repo.

###### AVAILABLE DETECTORS:
* [FemaleDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/femalewords)
* [MaleDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/malewords)
* [GenderedWordDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/genderedwords)
* [PersonalLifeDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/personal_life)
  * Letters for women are more likely to discuss personal life.
* [PublicationDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/publications)
  * Letters for women are less likely to mention publications and projects
    * **Goal:** Develop code that can read text for details (numbers of publications, mention of participation and contribution to project(s)). If the text fails to mention of publications and projects or details are absent, return a summary statement that directs the author to mention publications and projects and include a description of them to strengthen the letter.
* [EffortDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/effort)
  * Letters for women are more likely to highlight effort (she is hard-working) instead of highlighting accomplishments (her research is groundbreaking).
* [GrindstoneDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/grindstone)
* [AgenticDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/agentic)
* [ConditionalSuperlativesDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/conditionalsuperlatives)
* [SuperlativeDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/superlatives)
  * Letters for women are less likely to contain superlatives (best, most, top, greatest). If they contain superlatives, they usually describe women in the context of emotional terms (she was the most compassionate).
    * **Goal:**  Develop code that can read text for superlatives. If the text lacks superlatives, return a summary statement that directs the author to add superlatives.
    * If superlatives are present, search for the adjectives or nouns associated with the superlative. If they are emotion or gendered terms (compassion), return a summary statement that directs the author to add superlatives that include accomplishments, skills, or capabilities.

###### INCOMPLETE DETECTORS:

* Repetition
  * Letters for men are far more likely to repeat positive words than letters for women: Here we found that the letters for women that had at least one of these terms had an average of 1.5 terms, whereas the letters for men that included at least one had an average of 2.0 such terms. That is, there was repetition of standout adjectives within men’s letters to a greater extent. (Trix & Psenka 2003, pg 18(208)
* Minimal Assurance
  * Letters for women are more likely to include minimal assurance (she can do the job) rather than a strong endorsement (he has all the necessary skills to excel in this position).
    * **Goal:** Develop code that can read text for minimal assurance. If the text includes minimum assurance statements, return a summary statement that directs the author to remove the minimal assurance and replace it a strong endorsement. If the text lacks strong endorsements, return a summary statement that directs the author to add one.
* Gender stereotypes for emotion-focused words (How is this different than communal?)
  * Letters for women are more likely to include gender stereotypes (she is compassionate vs he is a leader) and emotion-focused words.
    * **Goal:** Develop code that can read text for words and gender stereotypes and highlight them (Word List). Return a summary statement that directs the author to review the highlighted words and evaluate whether they are relevant for the recommendation or evaluation. If the emotion-focused words are relevant to the letter or evaluation, suggest that the author include additional statements that balance them out and highlight other relevant areas like skills and accomplishments.
    * *Note on the word list:* some of the words are incomplete, for example "shar" is included so that it  captures sharing or shared or share.
* Adjective Usage
  * Letters for women are more likely to use adjectives instead of nouns
    * **Goal:** Develop code that can read text for the presence of nouns that highlight roles/positions (like leader, researcher). If position nouns are absent, return a summary statement that directs the author to consider using nouns to strengthen the letter.
    * This one can be complicated. The goal is to differentiate between descriptions that use adjectives, verbs, or weaken the position noun (i.e., she was involved in research, she taught).


## Getting Started

A note on using macOS. There can be some difficulty in getting

```
genderbias -h
```
to work in the terminal if using a newer version on macOS. Make sure to configure the PATH to contain
genderbias and where you stored the requirements. In order to do this, newer versions use zsh instead of bash so you want to update *.zshrc* instead of *.bashrc* or *.bash_profile*.

To determine what shell you are using, run the command
```
echo $SHELL
```

### How to Run Detectors

Detectors can be run individually by specifying what detector you want to run.

A list of detectors can be displayed through the command

```
genderbias --list-detectors
```
1. You can run them on files by
```
genderbias -f ./example_letters/letterofRecW --detectors  Detector    
```
where you can specify the path to a file and multiple or one detector to run.

2. You can run them on text in the terminal through using
```
echo "insert text here" | genderbias --detector Detector
```
and insert the text you want to eest and be sure to change Detector to a specific detector.


### How to Write Detectors

There is a lovely guide for writing new detectors linked [here](https://github.com/gender-bias/gender-bias/tree/master/docs/hacking). It was created by [Jordan Matelsky](https://github.com/j6k4m8) for those who are interested in either writing new detectors or understanding the code for the existing detectors.

## Help

Open a new issue for any questions and it will be addressed as quickly as possible. Also, feel free to contact the creators for clarification or if something is no longer working.


## Authors
Project started by Mollie Marr with Jordan Matelsky being a main contributor.

This read me was authored by [Alex Richter](https://github.com/ajrichter7) (she/her).
