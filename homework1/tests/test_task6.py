#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task6 import countWords


import pytest



sample_text = """Lorem ipsum dolor sit amet , consectetur adipiscing elit . Duis vitae feugiat
tortor , quis tempus lacus . Maecenas sollicitudin rhoncus ultricies .
Mauris neque metus , blandit sed sagittis aliquam , fringilla eget massa .
Donec at luctus leo . Curabitur suscipit nulla aliquam sapien maximus ,
sit amet fermentum sem malesuada . Nulla suscipit , felis non consequat
eleifend , sem quam pharetra turpis , vel efficitur tellus est placerat
est . Nam metus orci , facilisis et ante sed , ultricies pulvinar lorem .
Phasellus eu ipsum sit amet ex auctor volutpat . Suspendisse ac turpis et
felis tristique facilisis vitae in diam . Donec maximus ex in lorem
auctor vulputate . Nulla finibus sodales ante , convallis gravida metus
iaculis id ."""


def test_word_count(tmp_path):
    # Create temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(sample_text)

    # Verify word count
    assert countWords(test_file) == 127

