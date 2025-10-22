from enum import Enum
import re

from htmlnode import HTMLNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    CODE = "code"
    HEADING = "heading"
    QUOTE = "quote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


MARKDOWN_REGEX = {
    BlockType.CODE:r"`{3}[\s\S]*`{3}",
    BlockType.QUOTE:r">.*(\n>.*)*",
    BlockType.HEADING:r"#{1,6} .+",
    BlockType.UNORDERED_LIST:r"- .*(\n- .*)*",
    BlockType.ORDERED_LIST:r"\d\. .*(\n\d\. .*)*"
}

def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = [b.strip() for b in markdown.split("\n\n") if len(b) > 0]
       
    return blocks

def block_to_block_type(block:str) -> BlockType:
    for md in MARKDOWN_REGEX:
        if re.match(MARKDOWN_REGEX[md], block):
            if md == BlockType.ORDERED_LIST:
                ordered = True
                nums = [int(r[0]) for r in block.split("\n")]
                if nums[0] != 1:
                    ordered = False
                for i in range(1, len(nums)):
                    if nums[i] != nums[i-1] + 1:
                        ordered = False
                if not ordered:
                    continue
            return md
    return BlockType.PARAGRAPH
