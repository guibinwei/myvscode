sounds_source = Dict(
    "game_over" => "https://themushroomkingdom.net/sounds/wav/smb/smb_gameover.wav",
    "stage_clear" => "https://themushroomkingdom.net/sounds/wav/smb/smb_stage_clear.wav",
    "coin" => "https://themushroomkingdom.net/sounds/wav/smb/smb_coin.wav"
)

mkpath("data")
for (fname, link) in sounds_source
    download(link, "data/$fname.wav")
end