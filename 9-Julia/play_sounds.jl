using WAV

sounds = Dict(
    (key, wavread("data/$key.wav")) for key in keys(sounds_source)
)

wavplay(sounds["game_over"][1], sounds["game_over"][2])