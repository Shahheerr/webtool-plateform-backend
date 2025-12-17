from agents import Agent, Runner, ModelSettings
from config.gemini_config import gemini_config, gemini_model

# --- Model Settings ---

# High creativity for storytelling, poetry, and ideation
creative_model_setting = ModelSettings(
    temperature=0.9,
    top_p=0.95
)

# Balanced for standard writing, emails, and essays
balanced_model_setting = ModelSettings(
    temperature=0.5,
    top_p=0.85
)

# precise for grammar, corrections, and factual tasks
precise_model_setting = ModelSettings(
    temperature=0.1,
    top_p=0.5
)

# --- Creative Agents ---

story_generator_agent = Agent(
    name="Story Generator",
    instructions=(
        "You are an expert Story Teller. Create captivating and imaginative stories based on the user's prompt. "
        "Focus on character development, setting, and plot progression. "
        "Ensure the tone matches the user's request."
    ),
    model=gemini_model,
    model_settings=creative_model_setting
)

poem_generator_agent = Agent(
    name="Poem Generator",
    instructions=(
        "You are a Poet. Write beautiful and evocative poems. "
        "Pay attention to rhythm, rhyme (if requested), and imagery. "
        "Adapt your style to the requested form (e.g., haiku, sonnet, free verse)."
    ),
    model=gemini_model,
    model_settings=creative_model_setting
)

backstory_generator_agent = Agent(
    name="Backstory Generator",
    instructions=(
        "You are a Character Designer. Create detailed and compelling backstories for characters. "
        "Include their motivations, past traumas, key life events, and personality traits."
    ),
    model=gemini_model,
    model_settings=creative_model_setting
)

slogan_generator_agent = Agent(
    name="Slogan Generator",
    instructions="Generate catchy, memorable, and impactful slogans for brands, products, or campaigns.",
    model=gemini_model,
    model_settings=creative_model_setting,
    output_type=list
)

caption_generator_agent = Agent(
    name="Caption Generator",
    instructions="Write engaging and relevant captions for social media posts, images, or videos. Include hashtags if appropriate.",
    model=gemini_model,
    model_settings=creative_model_setting
)

message_generator_agent = Agent(
    name="Message Generator",
    instructions="Draft clear, thoughtful, and appropriate messages for various contexts (personal, professional, casual).",
    model=gemini_model,
    model_settings=creative_model_setting
)

reply_generator_agent = Agent(
    name="Reply Generator",
    instructions="Compose polite, witty, or professional replies to received messages or comments.",
    model=gemini_model,
    model_settings=creative_model_setting
)

business_name_generator_agent = Agent(
    name="Business Name Generator",
    instructions="Generate creative and unique business names. Provide the top 3 options.",
    model=gemini_model,
    output_type=list
)

book_title_generator_agent = Agent(
    name="Book Title Generator",
    instructions="Generate intriguing and marketable book titles. Provide the top 3 options.",
    model=gemini_model,
    output_type=list
)

# --- Writing & Content Agents (Balanced) ---

cover_letter_generator_agent = Agent(
    name="Cover Letter Generator",
    instructions=(
        "You are a Career Coach. Write professional and persuasive cover letters. "
        "Highlight the candidate's skills and experience relevant to the job description."
    ),
    model=gemini_model,
    model_settings=balanced_model_setting
)

email_writer_agent = Agent(
    name="Email Writer",
    instructions="Write clear, concise, and professional emails for business or personal communication.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

essay_writer_agent = Agent(
    name="Essay Writer",
    instructions=(
        "You are an Academic Writer. Write well-structured essays with a clear introduction, body paragraphs, and conclusion. "
        "Support arguments with logical reasoning."
    ),
    model=gemini_model,
    model_settings=balanced_model_setting
)

article_rewriter_agent = Agent(
    name="Article Rewriter",
    instructions="Rewrite articles or text to improve flow, clarity, and engagement while retaining the original meaning.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

review_generator_agent = Agent(
    name="Review Generator",
    instructions="Write balanced and informative reviews for products, services, books, or movies.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

paragraph_generator_agent = Agent(
    name="Paragraph Generator",
    instructions="Write coherent and well-structured paragraphs on a given topic.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

paragraph_expander_agent = Agent(
    name="Paragraph Expander",
    instructions="Expand on short paragraphs or ideas, adding details, examples, and depth.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

sentence_expander_agent = Agent(
    name="Sentence Expander",
    instructions="Expand simple sentences into more descriptive and complex ones without losing the original message.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

humanize_ai_agent = Agent(
    name="Humanize AI",
    instructions="Rewrite AI-generated text to sound more natural, conversational, and human-like.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

conclusion_writer_agent = Agent(
    name="Conclusion Writer",
    instructions="Write strong and memorable conclusions that summarize main points and provide closure.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

ai_prompt_generator_agent = Agent(
    name="AI Prompt Generator",
    instructions="Design detailed and effective prompts to guide AI models for specific tasks.",
    model=gemini_model,
    model_settings=balanced_model_setting
)

# --- Precise & Structural Agents (Low Temp) ---

outline_generator_agent = Agent(
    name="Outline Generator",
    instructions="Create structured outlines for essays, articles, projects, or presentations. Use bullets and hierarchy.",
    model=gemini_model,
    model_settings=precise_model_setting
)

answer_generator_agent = Agent(
    name="Answer Generator",
    instructions="Provide direct, accurate, and concise answers to questions.",
    model=gemini_model,
    model_settings=precise_model_setting
)

thesis_statement_generator_agent = Agent(
    name="Thesis Statement Generator",
    instructions="Draft clear and arguable thesis statements for academic papers.",
    model=gemini_model,
    model_settings=precise_model_setting
)

faq_generator_agent = Agent(
    name="FAQ Generator",
    instructions="Generate a list of Frequently Asked Questions (FAQs) and answers relevant to the topic.",
    model=gemini_model,
    model_settings=precise_model_setting
)

acronym_generator_agent = Agent(
    name="Acronym Generator",
    instructions="Create creative and meaningful acronyms for phrases or project names.",
    model=gemini_model,
    model_settings=precise_model_setting
)

meta_description_generator_agent = Agent(
    name="Meta Description Generator",
    instructions="Write SEO-friendly meta descriptions (approx 150-160 chars) that summarize content effectively.",
    model=gemini_model,
    model_settings=precise_model_setting
)

small_text_generator_agent = Agent(
    name="Small Text Generator",
    instructions="Generate short, punchy text snippets or blurbs.",
    model=gemini_model,
    model_settings=precise_model_setting
)

spell_checker_agent = Agent(
    name="Spell Checker",
    instructions="Identify and correct spelling errors in the provided text. Return the corrected text.",
    model=gemini_model,
    model_settings=precise_model_setting
)

grammar_checker_agent = Agent(
    name="Grammar Checker",
    instructions="Identify and fix grammatical errors, punctuation issues, and awkward phrasing. Return the corrected text.",
    model=gemini_model,
    model_settings=precise_model_setting
)

sentence_shortener_agent = Agent(
    name="Sentence Shortener",
    instructions="Condense long sentences into concise versions while preserving the core meaning.",
    model=gemini_model,
    model_settings=precise_model_setting
)

sentence_generator_agent = Agent(
    name="Sentence Generator",
    instructions="Generate individual sentences based on keywords or context provided.",
    model=gemini_model,
    model_settings=precise_model_setting
)