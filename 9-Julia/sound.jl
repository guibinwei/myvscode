using FileIO: load, save, loadstreaming, savestreaming
using LibSndFile
using WAV

sounds_source = Dict(
    "game_over" => "https://themushroomkingdom.net/sounds/wav/smb/smb_gameover.wav",
    "stage_clear" => "https://themushroomkingdom.net/sounds/wav/smb/smb_stage_clear.wav",
    "coin" => "https://themushroomkingdom.net/sounds/wav/smb/smb_coin.wav"
)



#=
mkpath("data")
for (fname, link) in sounds_source
    download(link, "data/$fname.wav")
end

=#

sounds = Dict(
    (key, wavread("data/$key.wav")) for key in keys(sounds_source)
)


wavplay(sounds["game_over"][1], sounds["game_over"][2])

save("data/radetzky_2.wav", x[0s..10s, :])