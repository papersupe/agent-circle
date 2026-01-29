# backend/rag/text_normalization.py
"""
text_normalization.py

Lightweight, deterministic text normalization utilities.

Goals:
- Improve readability of extracted PDF text
- Preserve original meaning
- Avoid aggressive or lossy transformations
- Be safe to apply before chunking & embedding

This module MUST NOT:
- Use ML or LLMs
- Reorder sentences
- Remove semantic content
"""

import re
import unicodedata


WHITESPACE_RE = re.compile(r"\s+")
BROKEN_WORD_RE = re.compile(r"([a-z])([A-Z])")
LINE_HYPHEN_RE = re.compile(r"-\n")


def normalize_unicode(text: str) -> str:
    """
    Normalize unicode characters into a consistent form.
    """
    return unicodedata.normalize("NFKC", text)


def fix_hyphenated_line_breaks(text: str) -> str:
    """
    Fix words broken across lines by hyphenation.

    Example:
        'inter-\naction' -> 'interaction'
    """
    return LINE_HYPHEN_RE.sub("", text)


def fix_missing_spaces(text: str) -> str:
    """
    Insert spaces between merged words caused by PDF extraction.

    Example:
        'ThisPaperIntroduces' -> 'This Paper Introduces'
    """
    return BROKEN_WORD_RE.sub(r"\1 \2", text)


def normalize_whitespace(text: str) -> str:
    """
    Collapse excessive whitespace while preserving paragraph breaks.
    """
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Preserve paragraph breaks
    paragraphs = [
        WHITESPACE_RE.sub(" ", p).strip()
        for p in text.split("\n\n")
        if p.strip()
    ]

    return "\n\n".join(paragraphs)


def normalize_text(text: str) -> str:
    """
    Primary normalization entry point.

    Safe to call from:
    - ingestion pipeline
    - chunk lookup
    - search response formatting
    """
    if not text or not isinstance(text, str):
        return ""

    text = normalize_unicode(text)
    text = fix_hyphenated_line_breaks(text)
    text = fix_missing_spaces(text)
    text = normalize_whitespace(text)

    return text
