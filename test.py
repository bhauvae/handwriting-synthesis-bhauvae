from demo import Hand
from data import wrapped_text
test = Hand()

lines = wrapped_text
biases = [.9 for i in lines]
styles = [1 for i in lines]
stroke_colors = ["black" for i in lines]
stroke_widths = [2 for i in lines]

test.write(
    filename='img/works.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
