# CHANGELOG

# v.1.3 [6th February 2022]
- Fixed a variable typo
- Fixed an issue in main logic which incorrectly referenced the wrong dictionary, causing a crash on write
- Added output bindings and associated logic for Cosmos DB

# v.1.2 [5th February 2022]
- Completely restructured the main logic to retrieve keywords and linked entites
- Improved error handling to fix a crash relating to lack of entities
- Reduced the amount of logging - keywords and entites are now shown in one log rather than a unique log per item
- Fixed a comment typo 

# v.1.1.1 [4th February 2022]
- Added an addition log at the end of execution
- Fixed a missing bracket which was causing a runtime error
- Removed root requirements.txt file

# v.1.1 [4th February 2022]
- Slightly changed formatting on README.md
- Added logic to get keywords and entity links to request body. Next version will focus on changing models and writing output to Cosmos

# v.1.0 [2nd February 2022]
- Added initial test implementation

<!-- {
    "id": "31886c7f-899e-4038-ywqt120984db1e",
    "title": "Thermal Properties of 1,847 WISE-observed Asteroids",
    "abstract": "We present new thermophysical model (TPM) fits of 1,847 asteroids, deriving\nthermal inertia, diameter, and Bond and visible geometric albedo. We use\nthermal flux measurements obtained by the Wide-field Infrared Survey Explorer\n(WISE; Wright et al. 2010; Mainzer et al. 2011) during its fully cryogenic\nphase, when both the 12$\\mu$m (W3) and 22$\\mu$m (W4) bands were available. We\ntake shape models and spin information from the Database of Asteroid Models\nfrom Inversion Techniques (DAMIT; \\v{D}urech et al. 2010) and derive new shape\nmodels through lightcurve inversion and combining WISE photometry with existing\nDAMIT lightcurves. When we limit our sample to the asteroids with the most\nreliable shape models and thermal flux measurements, we find broadly consistent\nthermal inertia relations with recent studies. We apply fits to the diameters\n$D$ (km) and thermal inertia $\\Gamma$ (J m$^{-2}$ s$^{-0.5}$ K$^{-1}$)\nnormalized to 1 au with a linear relation of the form\n$\\log[\\Gamma]=\\alpha+\\beta\\log[D]$, where we find $\\alpha = 2.667 \\pm 0.059$\nand $\\beta = -0.467 \\pm 0.044$ for our sample alone and $\\alpha = 2.509 \\pm\n0.017$ and $\\beta = -0.352 \\pm 0.012$ when combined with other literature\nestimates. We find little evidence of any correlation between rotation period\nand thermal inertia, owing to the small number of slow rotators to consider in\nour sample. While the large uncertainties on the majority of our derived\nthermal inertia only allow us to identify broad trends between thermal inertia\nand other physical parameters, we can expect a significant increase in\nhigh-quality thermal flux measurements and asteroid shape models with upcoming\ninfrared and wide-field surveys, enabling even more thermophysical modeling of\nhigher precision in the future.",
    "authors": [
        "Denise Hung",
        "Josef Hanuš",
        "Joseph R. Masiero",
        "David J. Tholen"
    ],
    "topics": [
        "Earth and Planetary Astrophysics"
    ],
    "likes": 0,
    "comments": 0,
    "keywords": [],
    "linked_topics": [],
    "url": "http://arxiv.org/pdf/2201.05164"
} -->