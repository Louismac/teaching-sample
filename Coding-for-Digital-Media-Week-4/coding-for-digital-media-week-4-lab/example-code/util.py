def draw_bars(dot, bars=2, beats=4):
    total_beats = bars * beats
    width = dot.width
    height = dot.height
    beat_spacing = width // total_beats
    bar_spacing = beat_spacing * beats
    for i in range(bars):
        # Draw bar line (thicker line for bars)
        x_pos_bar = i * bar_spacing
        dot.set_stroke_weight(8)
        dot.stroke(dot.red)
        dot.line((x_pos_bar, 0), (x_pos_bar, height))
        # Draw beat lines within each bar (thinner lines for beats)
        dot.set_stroke_weight(3)
        dot.stroke(dot.blue)
        for j in range(1, beats):
            x_pos_beat = x_pos_bar + j * beat_spacing
            dot.line((x_pos_beat, 0), (x_pos_beat, height))