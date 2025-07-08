\# LLM Red Teaming Dashboard: Fortifying AI Safety



\## Project Overview: Pioneering Proactive AI Safety Against Catastrophic Risks



This project introduces an advanced \*\*LLM Red Teaming Dashboard\*\*, a robust tool meticulously designed to systematically test and enhance the safety and ethical alignment of Large Language Models (LLMs). Building upon fundamental red teaming principles, this iteration significantly deepens its focus to identify and mitigate \*\*high-severity, real-world vulnerabilities\*\*. This includes scenarios where LLMs might generate content related to illicit substance synthesis, advanced biological/chemical weapons, or incitement to violence.



By automating the generation of sophisticated adversarial prompts, rigorously evaluating LLM responses with an AI judge, and visualizing the results through an interactive dashboard, this project delivers a practical and scalable framework for proactive AI safety engineering. It highlights the intricate challenges of \*\*prompt engineering\*\* in preventing the catastrophic misuse of powerful AI models.



\## Features



This dashboard integrates several key components to create a comprehensive and automated red-teaming pipeline:



1\.  \*\*Targeted Adversarial Prompt Generation (`prompt\_generator.py`):\*\*

&nbsp;   \* \*\*Purpose:\*\* To create subtle yet potent prompts designed to bypass conventional LLM safety mechanisms.

&nbsp;   \* \*\*Mechanism:\*\* Leverages `Google Gemini 1.5 Flash` to intelligently generate diverse adversarial variations from sensitive "seed concepts." This component is specifically engineered to explore critical vulnerabilities, crafting requests that appear innocuous while attempting to elicit harmful outputs (e.g., precise instructions for illegal synthesis disguised as academic inquiry or fictional scenarios).



2\.  \*\*Target LLM Interaction:\*\*

&nbsp;   \* \*\*Purpose:\*\* To observe and capture the behavior of an LLM when confronted with these high-stakes adversarial prompts.

&nbsp;   \* \*\*Mechanism:\*\* Each generated adversarial prompt is sent to a `Google Gemini 1.5 Flash` model (designated as the "Target LLM"). The model's responses are meticulously recorded for subsequent evaluation.



3\.  \*\*Constitutional AI Judge (`jailbreak\_scorer.py`):\*\*

&nbsp;   \* \*\*Purpose:\*\* To objectively and consistently assess the safety and ethical alignment of the Target LLM's responses.

&nbsp;   \* \*\*Mechanism:\*\* An independent `Google Gemini 1.5 Flash` instance serves as the "Judge AI." It operates under a pre-defined set of ethical "constitutional principles" (e.g., harmlessness, clear refusal to malicious prompts, avoidance of detailed harmful instructions). The Judge assigns a numerical score (0-100) to each response and provides detailed, transparent reasoning, indicating specific principle violations or adherence. This automates the critical safety auditing process.



4\.  \*\*Interactive Web Dashboard (`app.py` \& `frontend/index.html`):\*\*

&nbsp;   \* \*\*Purpose:\*\* To visualize, analyze, and explore the results of the red-teaming campaigns.

&nbsp;   \* \*\*Mechanism:\*\* A `Python Flask` backend reads the collected `red\_teaming\_campaign\_results.csv` data and serves it as a JSON API. A `React.js` frontend consumes this data, presenting it through a dynamic, sortable, and searchable table, alongside a `Chart.js` powered bar chart that visually represents the distribution of safety scores.



\## Technical Stack



\* \*\*Python 3.x:\*\* Core programming language for all backend logic, LLM integrations, and data processing.

&nbsp;   \* `Flask`: Lightweight web framework for the backend API server.

&nbsp;   \* `pandas`: Essential for efficient reading, writing, and manipulation of CSV data.

&nbsp;   \* `google-generativeai`: The official Python SDK for seamless interaction with the Google Gemini API.

&nbsp;   \* `python-dotenv`: Ensures secure loading and management of API keys from a `.env` file.

&nbsp;   \* `Flask-Cors`: Handles Cross-Origin Resource Sharing, enabling smooth communication between the Flask backend and the React frontend.

\* \*\*JavaScript (Frontend):\*\*

&nbsp;   \* `React.js` (loaded via CDN): A declarative JavaScript library for building the user interface components of the dashboard.

&nbsp;   \* `Chart.js`: A versatile JavaScript library used for creating the responsive and interactive bar chart visualization of safety scores.

\* \*\*Google Gemini API:\*\* Utilized extensively throughout the project, specifically the `gemini-1.5-flash` model, for its balance of performance, speed, and cost-effectiveness.



\## Setup and Installation



To get this project running locally on your machine, follow these steps:



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/YourGitHubUsername/LLM-Red-Teaming-Dashboard.git](https://github.com/YourGitHubUsername/LLM-Red-Teaming-Dashboard.git)

&nbsp;   cd LLM-Red-Teaming-Dashboard

&nbsp;   ```

&nbsp;   \*(\*\*Important:\*\* Replace `YourGitHubUsername` with your actual GitHub username)\*



2\.  \*\*Create and activate a Python virtual environment:\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   # On Windows:

&nbsp;   .\\venv\\Scripts\\activate

&nbsp;   # On macOS/Linux:

&nbsp;   source venv/bin/activate

&nbsp;   ```



3\.  \*\*Install project dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\.  \*\*Set up your Google Gemini API Key:\*\*

&nbsp;   \* Obtain a Google Gemini API key from the \[Google AI Studio](https://ai.google.dev/aistudio).

&nbsp;   \* Create a new file named `.env` in the root of your project directory (the same folder where `app.py` and `red\_teaming\_orchestrator.py` are located).

&nbsp;   \* Add your API key to the `.env` file in the following format:

&nbsp;       ```

&nbsp;       GOOGLE\_API\_KEY="YOUR\_ACTUAL\_API\_KEY\_HERE"

&nbsp;       ```

&nbsp;       \*(\*\*Remember to replace `YOUR\_ACTUAL\_API\_KEY\_HERE` with your unique key.\*\*)\*

&nbsp;   \* \*\*Security Note:\*\* The `.env` file is explicitly listed in the `.gitignore` and will \*\*not\*\* be uploaded to GitHub, ensuring your API key remains confidential.



\## How to Run the Red Teaming Campaign and Dashboard



1\.  \*\*Run the Red Teaming Orchestrator:\*\*

&nbsp;   This script initiates the entire red-teaming campaign. It will generate adversarial prompts based on internal seed prompts, send them to the target LLM, and then have the Judge AI score the responses. All results are saved to `red\_teaming\_campaign\_results.csv`.



&nbsp;   ```bash

&nbsp;   python red\_teaming\_orchestrator.py

&nbsp;   ```

&nbsp;   \* \*\*API Quota Awareness:\*\* The Google Gemini API (especially on the free tier) has daily rate limits (e.g., typically 50 requests/day per model for `gemini-1.5-flash`). The `red\_teaming\_orchestrator.py` includes built-in `time.sleep()` delays and processes a limited number of seed prompts/variants to help manage these limits. For more extensive or continuous testing, consider enabling billing in your Google AI Studio project to increase your quota.



2\.  \*\*Run the Dashboard:\*\*

&nbsp;   Once the `red\_teaming\_orchestrator.py` has completed and populated your `red\_teaming\_campaign\_results.csv` file, you can start the dashboard. This will launch a local web server to host your interactive dashboard.



&nbsp;   ```bash

&nbsp;   python app.py

&nbsp;   ```

&nbsp;   You will see a message in your terminal indicating the server is running, usually at `http://127.0.0.1:5000/`. Open this URL in your web browser to access your dashboard.



\## Project Insights and Findings



This recent iteration of the project, with its sharpened focus on catastrophic vulnerabilities, yielded critical insights into the real-world safety performance of LLMs:



\* \*\*Robustness Against Direct Harmful Queries:\*\* The `Google Gemini 1.5 Flash` model consistently demonstrated strong inherent safety filters, providing clear refusals when directly prompted for illicit substance synthesis or explicit instructions for lethal outputs. This confirms a significant baseline defense.

\* \*\*Challenges with Nuanced \& Disguised Prompts:\*\* While direct harmful generations were largely averted, the adversarial prompt generator successfully crafted highly subtle and disguised requests (e.g., framing dangerous instructions as "fictional scenarios," "academic research," or "historical analysis"). These nuanced prompts sometimes elicited responses that, while including disclaimers, still contained detailed information that could be problematic in a less secure context. This underscores the persistent challenge of balancing LLM helpfulness with absolute safety.

\* \*\*Effectiveness of AI-Driven Auditing:\*\* The Constitutional AI Judge proved invaluable in this advanced red-teaming. It consistently identified and accurately scored even the most nuanced compromises, providing detailed reasoning that went beyond simple content blocking. This solidifies the efficacy and necessity of using AI to audit AI for complex ethical and safety violations.

\* \*\*The Imperative of Continuous Vigilance:\*\* This campaign powerfully demonstrated that AI safety is not a static state but an ongoing, dynamic process. Automated red teaming is indispensable for continuously monitoring model behavior as LLMs evolve, new adversarial techniques emerge, and new applications are developed.



\*(\*\*Optional: Insert screenshots/GIFs of your dashboard here!\*\* Make sure these are hosted publicly, e.g., by committing them to your GitHub repo in an `images/` folder and linking to them like this: `!\[Dashboard Bar Chart](images/your\_bar\_chart.png)`)\*



\*Example Screenshot: Distribution of safety scores across various prompt types after a campaign run.\*

!\[Dashboard Bar Chart Example](https://placehold.co/800x400/cccccc/333333?text=YOUR\_DASHBOARD\_BAR\_CHART\_SCREENSHOT)



\*Example Screenshot: Detailed table view showing an adversarial prompt, LLM response, score, and Judge's reasoning.\*

!\[Dashboard Table Example](https://placehold.co/800x400/cccccc/333333?text=YOUR\_DASHBOARD\_TABLE\_SCREENSHOT)



\## Contributing



Contributions, issues, and feature requests are highly welcome! Feel free to fork this repository, open issues to report bugs or suggest enhancements, or submit pull requests with improvements.



\## License



This project is open-sourced under the \[MIT License](https://opensource.org/licenses/MIT).



---

