"""
Agent Registry Module
Central registry for all AI agents and deterministic tools.
"""
from typing import Optional, Union, Callable
from agents import Agent

from Agents.generation_agent import (
    story_generator_agent, poem_generator_agent, backstory_generator_agent,
    slogan_generator_agent, caption_generator_agent, message_generator_agent,
    reply_generator_agent, business_name_generator_agent, book_title_generator_agent,
    cover_letter_generator_agent, email_writer_agent, essay_writer_agent,
    article_rewriter_agent, review_generator_agent, paragraph_generator_agent,
    paragraph_expander_agent, sentence_expander_agent, humanize_ai_agent,
    conclusion_writer_agent, ai_prompt_generator_agent, outline_generator_agent,
    answer_generator_agent, thesis_statement_generator_agent, faq_generator_agent,
    acronym_generator_agent, meta_description_generator_agent, small_text_generator_agent,
    spell_checker_agent, grammar_checker_agent, sentence_shortener_agent,
    sentence_generator_agent
)


# ============= DETERMINISTIC TOOLS =============
def hex_to_rgb_logic(input_data: str) -> str:
    """Convert hex color to RGB format."""
    hex_val = input_data.lstrip('#').strip()
    try:
        if len(hex_val) not in [3, 6]:
            return "Invalid Hex Code: Must be 3 or 6 characters"
        if len(hex_val) == 3:
            hex_val = ''.join([c*2 for c in hex_val])
        r = int(hex_val[0:2], 16)
        g = int(hex_val[2:4], 16)
        b = int(hex_val[4:6], 16)
        return f"rgb({r}, {g}, {b})"
    except ValueError:
        return "Invalid Hex Code: Contains non-hex characters"


def code_beautifier_logic(input_data: str) -> str:
    """Beautify code with proper formatting."""
    lines = input_data.strip().split('\n')
    beautified = '\n'.join(line.rstrip() for line in lines)
    return f"// Beautified Code\n{beautified}\n// End"


def domain_checker_logic(input_data: str) -> str:
    """Check domain availability (mock implementation)."""
    domain = input_data.strip().lower().replace(' ', '')
    if not domain:
        return "Please provide a domain name"
    return f"Domain '{domain}.com' is available! (Mock Response)"


def plagiarism_checker_logic(input_data: str) -> str:
    """Check for plagiarism (mock implementation)."""
    text = input_data.strip()
    if not text:
        return "Please provide text to check"
    word_count = len(text.split())
    return f"Plagiarism Check Complete. Originality Score: 95%. Words Processed: {word_count}."


# ============= AGENT REGISTRY =============
# Maps slug -> Agent instance (for AI-powered tools)
AGENT_REGISTRY = {
    # Creative Agents
    "story-generator": story_generator_agent,
    "ai-story-generator": story_generator_agent,
    "poem-generator": poem_generator_agent,
    "backstory-generator": backstory_generator_agent,
    "slogan-generator": slogan_generator_agent,
    "caption-generator": caption_generator_agent,
    "message-generator": message_generator_agent,
    "reply-generator": reply_generator_agent,
    "business-name-generator": business_name_generator_agent,
    "book-title-generator": book_title_generator_agent,
    
    # Writing & Content Agents
    "cover-letter-generator": cover_letter_generator_agent,
    "email-writer": email_writer_agent,
    "essay-writer": essay_writer_agent,
    "article-rewriter": article_rewriter_agent,
    "ai-content-improver": article_rewriter_agent,
    "review-generator": review_generator_agent,
    "paragraph-generator": paragraph_generator_agent,
    "paragraph-expander": paragraph_expander_agent,
    "sentence-expander": sentence_expander_agent,
    "humanize-ai": humanize_ai_agent,
    "conclusion-writer": conclusion_writer_agent,
    "ai-prompt-generator": ai_prompt_generator_agent,
    
    # Precise & Structural Agents
    "outline-generator": outline_generator_agent,
    "answer-generator": answer_generator_agent,
    "thesis-statement-generator": thesis_statement_generator_agent,
    "faq-generator": faq_generator_agent,
    "acronym-generator": acronym_generator_agent,
    "meta-description-generator": meta_description_generator_agent,
    "meta-tag-generator": meta_description_generator_agent,
    "small-text-generator": small_text_generator_agent,
    "spell-checker": spell_checker_agent,
    "grammar-checker": grammar_checker_agent,
    "sentence-shortener": sentence_shortener_agent,
    "sentence-generator": sentence_generator_agent,
}

# ============= TOOL REGISTRY =============
# Maps slug -> callable function (for deterministic tools)
TOOL_REGISTRY = {
    "hex-to-rgb": hex_to_rgb_logic,
    "code-beautifier": code_beautifier_logic,
    "domain-checker": domain_checker_logic,
    "plagiarism-checker": plagiarism_checker_logic,
}

# ============= UNIFIED REGISTRY =============
# Combined registry for all tools (agents + deterministic)
UNIFIED_REGISTRY = {**AGENT_REGISTRY, **TOOL_REGISTRY}


def get_agent(slug: str) -> Optional[Agent]:
    """Get an AI agent by slug."""
    return AGENT_REGISTRY.get(slug)


def get_tool(slug: str) -> Optional[Callable]:
    """Get a deterministic tool by slug."""
    return TOOL_REGISTRY.get(slug)


def get_agent_or_tool(slug: str) -> Optional[Union[Agent, Callable]]:
    """Get any handler (agent or tool) by slug."""
    return UNIFIED_REGISTRY.get(slug)


def get_all_agent_slugs() -> list:
    """Get all AI agent slugs."""
    return list(AGENT_REGISTRY.keys())


def get_all_tool_slugs() -> list:
    """Get all deterministic tool slugs."""
    return list(TOOL_REGISTRY.keys())


def get_all_slugs() -> list:
    """Get all available slugs (agents + tools)."""
    return list(UNIFIED_REGISTRY.keys())