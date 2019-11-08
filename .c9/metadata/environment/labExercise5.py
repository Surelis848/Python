{"changed":true,"filter":false,"title":"labExercise5.py","tooltip":"/labExercise5.py","value":"with open(\"static/hnr1.abc\", \"r\") as raw_data:\n    song_line = \"\"\n    # Read each line in the file and check for the characters which denote each piece of information we require\n    # Store the information as a variable and add it to the song_line\n    # Once we find a new song (by detecting the line contains X:), wipe out the temp_title variable\n    for line in raw_data:\n        if \"X:\" in line:\n            temp_title = \"\"\n            song_index = line[2:-1:]\n            song_line += (song_index + \"...\")\n        elif \"T:\" in line:\n            # Check if T: already exists in our temp_title variable, meaning we have already captured the title for this\n            # song. If found, continue out of the loop (skipping the else statement on line 58)\n            if \"T:\" in temp_title:\n                continue\n            else:\n                # If T: was not found in the temp_title, then capture it in temp_title as is and in title with the\n                # correct formatting\n                temp_title = line\n                title = line[2:-1:]\n                song_line += (title + \"...\")\n        elif \"M:\" in line:\n            key_sig = line[2:-1:]\n            song_line += (\"Key Sig: \" + key_sig + \"...\")\n        elif \"K:\" in line:\n            time_sig = line[2::]\n            song_line += (\"Time Sig: \" + time_sig)\n    print(song_line)\n\"\"\"\nwith open(\"static/hnr1.abc\", \"r\") as musicfile:\n    title=''\n    for line in musicfile:\n        if line.startswith('X'):\n            id=line\n            title+=line\n\"\"\"\n        \n\"\"\"\nif f.mode == \"r\":\n    fl =f.readlines()\n    for x in fl:\n        if x.startswith(\"X\"):\n            print(x)\n        elif x.startswith(\"T\"):\n            print(x)\n        elif x.startswith(\"M\"):\n            print(\"Time sig:\", x)\n        elif x.startswith(\"K\"):\n            print(\"Key sig:\", x)\n\"\"\"","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":[" "],"id":155}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["x"],"id":156}],[{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":[","],"id":157}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":33},"action":"remove","lines":[" {x}\""],"id":158},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["\""]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":[" "],"id":159}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":[" "],"id":160}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":[","],"id":161}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":[" "],"id":162},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["x"]}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":[" "],"id":163},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["a"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["n"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":[" "],"id":164},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["x"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["."]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["e"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["n"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["s"],"id":165},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["w"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["="]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["="]}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"remove","lines":["="],"id":166},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"remove","lines":["="]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"remove","lines":["w"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"remove","lines":["s"]}],[{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["w"],"id":167},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["i"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["t"]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["h"]},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["("]}],[{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"insert","lines":[")"],"id":168}],[{"start":{"row":4,"column":43},"end":{"row":4,"column":45},"action":"insert","lines":["\"\""],"id":169}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":46},"action":"remove","lines":[" and x.endwith(\"\")"],"id":170}],[{"start":{"row":11,"column":32},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":171},{"start":{"row":12,"column":0},"end":{"row":12,"column":12},"action":"insert","lines":["            "]},{"start":{"row":12,"column":12},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":12},"action":"remove","lines":["    "],"id":172},{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["m"],"id":173},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":[" "],"id":174}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":[" "],"id":175}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["_"],"id":176},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["s"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["t"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["2"],"id":177}],[{"start":{"row":13,"column":8},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":178},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["y"],"id":179},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["_"]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["s"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["t"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["="],"id":180},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["3"]}],[{"start":{"row":14,"column":8},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":181},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["p"]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["r"]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":["i"]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":["n"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":7},"action":"insert","lines":["()"],"id":182}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["m"],"id":183},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":8},"action":"remove","lines":["my"],"id":184},{"start":{"row":15,"column":6},"end":{"row":15,"column":12},"action":"insert","lines":["my_str"]}],[{"start":{"row":12,"column":1},"end":{"row":15,"column":13},"action":"remove","lines":["           ","my_str=2","my_str=3","print(my_str)"],"id":185},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":13},"action":"insert","lines":["            ","my_str=2","my_str=3","print(my_str)"],"id":186}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":13},"action":"remove","lines":["            ","my_str=2","my_str=3","print(my_str)"],"id":187}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["2"],"id":188},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["2"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["2"]}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["2"],"id":189},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["2"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["2"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["\""],"id":190},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["\""]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["\""]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["\"\""],"id":191}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["\""],"id":192}],[{"start":{"row":1,"column":3},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":193}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"remove","lines":["f="],"id":194},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["w"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["i"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["t"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["h"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":195}],[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":[" "],"id":196},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["a"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":197}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["m"],"id":198},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["u"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["s"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["i"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["c"]},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["f"]},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["i"]},{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["l"]},{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":46},"end":{"row":0,"column":47},"action":"insert","lines":[":"],"id":199}],[{"start":{"row":0,"column":47},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["f"],"id":201},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["o"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":[" "],"id":202},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":[" "],"id":203},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["i"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":[" "],"id":204},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["m"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["i"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["s"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["i"]}],[{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["i"],"id":205},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["s"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["i"]}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["u"],"id":206},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["s"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["i"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":[" "],"id":207}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":[" "],"id":208}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["f"],"id":209}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":19},"action":"remove","lines":["musicf"],"id":210},{"start":{"row":1,"column":13},"end":{"row":1,"column":22},"action":"insert","lines":["musicfile"]}],[{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":[":"],"id":211}],[{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":212},{"start":{"row":2,"column":0},"end":{"row":2,"column":8},"action":"insert","lines":["        "]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["p"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["r"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["i"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["n"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":[" "],"id":213},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["e"],"id":214},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":[" "]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":15},"action":"insert","lines":["()"],"id":215}],[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["e"],"id":216}],[{"start":{"row":2,"column":16},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":217},{"start":{"row":3,"column":0},"end":{"row":3,"column":8},"action":"insert","lines":["        "]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["b"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["r"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["a"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["k"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["k"],"id":218},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":["a"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["e"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["r"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["e"],"id":219}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":16},"action":"remove","lines":["print(e)"],"id":220}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["l"],"id":221},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["i"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["n"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["i"],"id":222},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["f"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":[" "],"id":223},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["l"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["i"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["n"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["."],"id":224},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["s"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["t"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["a"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":20},"action":"remove","lines":["star"],"id":225},{"start":{"row":2,"column":16},"end":{"row":2,"column":28},"action":"insert","lines":["startswith()"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":29},"action":"insert","lines":["''"],"id":226}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["X"],"id":227}],[{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":[":"],"id":228}],[{"start":{"row":2,"column":32},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":229},{"start":{"row":3,"column":0},"end":{"row":3,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":0,"column":47},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":230},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["t"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["i"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["l"],"id":231},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["="],"id":232}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":12},"action":"insert","lines":["''"],"id":233}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["t"],"id":234},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["i"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["l"],"id":235},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["="],"id":236},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["t"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["i"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["l"],"id":237},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["+"],"id":238},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["l"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["i"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["n"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"remove","lines":["e"],"id":239},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"remove","lines":["n"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"remove","lines":["i"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["l"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["+"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["e"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["l"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["t"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"remove","lines":["i"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"remove","lines":["t"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"remove","lines":["="]}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["+"],"id":240},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["l"],"id":241},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["i"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["n"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":32},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":242},{"start":{"row":4,"column":0},"end":{"row":4,"column":12},"action":"insert","lines":["            "]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["i"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["="],"id":243},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["l"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["i"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["n"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["\""],"id":244},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["\""]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["\""]}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":245}],[{"start":{"row":6,"column":23},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":246},{"start":{"row":7,"column":0},"end":{"row":7,"column":12},"action":"insert","lines":["            "]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["\""]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["\""]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["\""]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["\""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":12},"action":"remove","lines":["            "],"id":247}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":248}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"remove","lines":["\""],"id":249}],[{"start":{"row":0,"column":0},"end":{"row":32,"column":20},"action":"insert","lines":["with open(\"Music.abc\", \"r\") as raw_data:","    song_index = int()","    title = \"\"","    temp_title = \"\"","    key_sig = \"\"","    time_sig = \"\"","    song_line = \"\"","    # Read each line in the file and check for the characters which denote each piece of information we require","    # Store the information as a variable and add it to the song_line","    # Once we find a new song (by detecting the line contains X:), wipe out the temp_title variable","    for line in raw_data:","        if \"X:\" in line:","            temp_title = \"\"","            song_index = line[2:-1:]","            song_line += (song_index + \"...\")","        elif \"T:\" in line:","            # Check if T: already exists in our temp_title variable, meaning we have already captured the title for this","            # song. If found, continue out of the loop (skipping the else statement on line 58)","            if \"T:\" in temp_title:","                continue","            else:","                # If T: was not found in the temp_title, then capture it in temp_title as is and in title with the","                # correct formatting","                temp_title = line","                title = line[2:-1:]","                song_line += (title + \"...\")","        elif \"M:\" in line:","            key_sig = line[2:-1:]","            song_line += (\"Key Sig: \" + key_sig + \"...\")","        elif \"K:\" in line:","            time_sig = line[2::]","            song_line += (\"Time Sig: \" + time_sig)","    print(song_line)"],"id":250}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":20},"action":"remove","lines":["Music.abc"],"id":251},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["h"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["n"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["r"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["1"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["."]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["a"],"id":252},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["b"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["s"],"id":253},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["t"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["a"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["t"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["i"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["c"]}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["/"],"id":254}],[{"start":{"row":1,"column":4},"end":{"row":5,"column":17},"action":"remove","lines":["song_index = int()","    title = \"\"","    temp_title = \"\"","    key_sig = \"\"","    time_sig = \"\""],"id":255},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"remove","lines":["    "]},{"start":{"row":0,"column":46},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":27},"action":"remove","lines":["            temp_title = \"\""],"id":256},{"start":{"row":6,"column":24},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":54},"end":{"row":23,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1571933925180}