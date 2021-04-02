tmps = map(float(input("ENTER TEMPERATURES SEPARATED BY A SPACE\n=> ")))
avg_tmp = (tmps[0] + tmps[1] + tmps[2] + tmps[3] +
           tmps[4] + tmps[5] + tmps[6]) / 7
print(f"Average temperature: {avg_tmp}")
