import json

with open("/home/samet/Projects/flyrank-ml-internship/work/notebooks/capstone.ipynb", "r") as f:
    notebook = json.load(f)

demo_outline_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 8. Showcase Demo Outline (5 minutes)\n\n",
        "- **Question (1 min):** How do we help content editors prioritize which pages to refresh before they crash in search rankings?\n",
        "- **Method (1 min):** We trained a Random Forest model on an anonymized dataset of content performance, strictly excluding future-window leakage and grouping splits by client to prove it generalizes.\n",
        "- **One Chart/Finding (1 min):** Showing the precision table: the model achieved a 0.86 Precision@50, beating the manual heuristic (0.42) which blindly flagged old pages even if they were evergreen.\n",
        "- **One Honest Result (1 min):** The model effectively identifies at-risk pages but completely breaks on seasonal traffic drops, acting as a decision-support tool rather than an automated CMS rule.\n",
        "- **One Recommendation (1 min):** Content teams should integrate this ranked queue to direct their weekly editorial roadmap, saving hours of manual spreadsheet analysis."
    ]
}

shareable_cuts_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 9. Shareable Cuts\n\n",
        "### Employer-Facing Summary (3 sentences)\n",
        "I built a machine learning ranking system to predict organic content decay for SEO teams, utilizing an anonymized sample of the FlyRank ML Internship dataset. By engineering historical traffic and engagement features while strictly isolating label leakage and validating via grouped splits, the Random Forest model identified high-risk pages with a Precision@50 of 0.86. This framework translates raw probabilities into a human-reviewed action playbook, vastly outperforming rigid manual heuristics and providing a scalable decision-support tool for content operations.\n\n",
        "### Social Post\n",
        "I recently completed my Capstone for the FlyRank ML Internship, tackling a classic SEO problem: how do you know a page is going to crash in search rankings before it happens? 📉\n\n",
        "Instead of relying on rigid rules (like 'refresh anything older than 180 days'), I trained a Random Forest classifier on historical engagement data. The hardest part wasn't the model—it was the validation. By using grouped splits to prevent the model from simply memorizing client domains, and ruthlessly hunting down label leakage, the model achieved a 0.86 Precision@50.\n\n",
        "The biggest takeaway? ML doesn't replace editors. The model still falls for seasonality traps! It acts as a targeted decision-support tool, helping human teams prioritize their weekly roadmap."
    ]
}

notebook["cells"].insert(-1, demo_outline_cell)
notebook["cells"].insert(-1, shareable_cuts_cell)

with open("/home/samet/Projects/flyrank-ml-internship/work/notebooks/capstone.ipynb", "w") as f:
    json.dump(notebook, f, indent=1)
