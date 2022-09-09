# Gender-bias (A Thesis Proposal)

## Problem:
Letters of recommendation are biased not only in terms of gender but also contain ethnic and racial bias. There is a large collection of research papers that show this is a problem [(Citations can be found here!)](https://drive.google.com/drive/folders/1J-Z8DU5IpA3pOYG4qYVTcDnyDvMKvyr7?usp=sharing) and also at the bottom of the repository for the gender-bias Github linked momentarily.

**Language:** Python and potentially Javascript to create a website

## Project:

This project is a [public repository](https://github.com/gender-bias/gender-bias) close to completion. Next steps include incorporating these detectors which are written in Python and deal with specific issues
that arise in letters of recommendation into an easy to use tool for researchers and
any person wishing to check their letters of recommendation. There are many avenues
that can be taken for this project which include:

- Completion of the final two detectors dealing with adjective usage and minimal assurance
in letters of recommendation. The description of all the detectors and the current state of each can be found
[here](https://github.com/ajrichter7/gender-bias/tree/master/genderbias). The detectors operate by using word lists. The difficulty in implementation deals with word lists
and accurately testing for these problems. Adjective usage detector implies that we can
count the number of adjectives for women vs men which might end up requiring a dataset
due to the comparison aspect. The minimal assurance detector requires a good understanding
of English grammar and can be hard with only word lists.
- Creation of a website that can process the letters easily allowing for a person to
copy and paste their letters in. This could include the option to run all detectors
on a letter or just specific ones possibly through buttons. Work has begun already
on a website but the status of which is unclear as it was done by undergraduates at Whitman
a few summers prior. The github to the webserver is included [here](https://github.com/gender-bias/gender-bias-web).
- Creation of a google docs plugin or Microsoft word plugin that runs similarly to the website.
Updating the detectors to use Natural Language Processing (NLP). Right now,
the detectors operate off of word lists which disregard context. This could
be an issue in phrasing and the detectors would identify some word as being
problematic but in a given context it could be okay. The problem with NLP
requires a database of anonymized letters of recommendation. One idea for
the database could be Rate My Professors [(a data set that exists is included here)](https://data.mendeley.com/datasets/fvtfjyvw7d/2).
Ideally we would use letters of recommendation written by professors but these
would need to be properly anonymized. A tool for anonymization that exists and
could serve as a jumping off point is included [here](https://github.com/microsoft/presidio) and has been created by Microsoft.
- Extending the detectors to check for racial and ethic biases. A collection of literature on this issue is included [here](https://github.com/ajrichter7/gender-bias/blob/master/thesis%20proposal/ethnicandracialbiasescitations.pdf)!

The **goal** of the project is to bring attention to this problem and also make it accessible to others. Right now the repository only works through terminal and requires a person to have at least basic knowledge of how to run a program. Ideally, this project will help people write better letters of recommendation through continual usage.

The repository that I created has the most up to date information on the detectors and has been the most recently updated. The original project was conceptualized and created in 2018. There was also a team of undergraduate researchers who worked on this project with Janet Davis at Whitman.

## Points of contact:

- Alex Richter ‘22 (alexis.richter7@gmail.com)
- Mollie Marr, the original creator of the Github repository and graduate student at OHSU (marmo@ohsu.edu)
- Anna Ritz (aritz@reed.edu)
- Janet Davis (davisj@whitman.edu)
