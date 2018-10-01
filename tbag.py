option = chr
rOneL = int
rOneR = int
rOneT = int
rOneD = int
rTwoL = int
rTwoR = int
rTwoT = int
rTwoD = int
walk_choice = chr
steps = int
ahead = chr
leftSteps = int
rightSteps = int
downSteps = int
topSteps = int
new_room = chr
room = ""
rOneL = 0
rOneR = 10
rOneT = 10
rOneD = 0
rTwoL = 0
rTwoR = 10
rTwoT = 5
rTwoD = 5
leftSteps = int(rOneL)
rightSteps = int(rOneR)
downSteps = int(rOneD)
topSteps = int(rOneT)
option = input("Do you want to enter Room I ? (y/n): ")
if option == 'y':
    print("Entered Room I !!!")
    room = "I"
    ahead = input("Do you want to go ahead ? (y/n): ")
    while ahead == 'y':
        if room == "I":
            if leftSteps == 10 and rightSteps == 0 and topSteps == 5 and downSteps == 5:
                new_room = input("Do you want to enter Room II ? (y/n): ")
                if new_room == 'y':
                    print("Entered Room II !!!")
                    room = "II"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 0
                        rightSteps = 10
                        topSteps = 5
                        downSteps = 5
                        continue
                    else:
                        break
            elif leftSteps == 0 and rightSteps == 10 and topSteps == 10 and downSteps == 0:
                new_room = input("Do you want to exit from Room I ? (y/n): ")
                if new_room == 'y':
                    print("Exited out of Room I...")
                    print("See you again...later :-)")
                    room = ""
                    break
        if room == "II":
            if leftSteps == 5 and rightSteps == 5 and topSteps == 0 and downSteps == 10:
                new_room = input("Do you want to enter Room III ? (y/n): ")
                if new_room == 'y':
                    print("Entered Room III !!!")
                    room = "III"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 5
                        rightSteps = 5
                        topSteps = 10
                        downSteps = 0
                        continue
                    else:
                        break
            elif leftSteps == 0 and rightSteps == 10 and topSteps == 5 and downSteps == 5:
                new_room = input("Do you want to return to Room I ? (y/n): ")
                if new_room == 'y':
                    print("returned to Room I...")
                    room = "I"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 10
                        rightSteps = 0
                        topSteps = 5
                        downSteps = 5
                        continue
                    else:
                        break
        if room == "III":
            if leftSteps == 0 and rightSteps == 10 and topSteps == 5 and downSteps == 5:
                new_room = input("Do you want to enter Room IV ? (y/n): ")
                if new_room == 'y':
                    print("Entered Room IV !!!")
                    room = "IV"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 10
                        rightSteps = 0
                        topSteps = 5
                        downSteps = 5
                        continue
                    else:
                        break
            elif leftSteps == 5 and rightSteps == 5 and topSteps == 10 and downSteps == 0:
                new_room = input("Do you want to return to Room II ? (y/n): ")
                if new_room == 'y':
                    print("Returned to Room II...")
                    room = "II"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 5
                        rightSteps = 5
                        topSteps = 0
                        downSteps = 10
                        continue
                    else:
                        break
        if room == "IV":
            if leftSteps == 0 and rightSteps == 10 and topSteps == 0 and downSteps == 10:
                new_room = input("Do you want to enter Room V ? (y/n): ")
                if new_room == 'y':
                    print("Entered Room V !!!")
                    room = "V"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 10
                        rightSteps = 0
                        topSteps = 0
                        downSteps = 10
                        continue
                    else:
                        break
            elif leftSteps == 10 and rightSteps == 0 and topSteps == 5 and downSteps == 5:
                new_room = input("Do you want to return to Room III ? (y/n): ")
                if new_room == 'y':
                    print("Returned to Room III...")
                    room = "III"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 0
                        rightSteps = 10
                        topSteps = 5
                        downSteps = 5
                        continue
                    else:
                        break
        if room == "V":
            if leftSteps == 5 and rightSteps == 5 and topSteps == 10 and downSteps == 0:
                new_room = input("Do you want to enter Room VI ? (y/n): ")
                if new_room == 'y':
                    print("Entered Room VI !!!")
                    room = "VI"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 5
                        rightSteps = 5
                        topSteps = 0
                        downSteps = 10
                        continue
                    else:
                        break
            elif leftSteps == 10 and rightSteps == 0 and topSteps == 0 and downSteps == 10:
                new_room = input("Do you want to returm to Room IV ? (y/n): ")
                if new_room == 'y':
                    print("Returned to Room IV...")
                    room = "IV"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 0
                        rightSteps = 10
                        topSteps = 0
                        downSteps = 10
                        continue
                    else:
                        break
        if room == "VI":
            if leftSteps == 5 and rightSteps == 5 and topSteps == 0 and downSteps == 10:
                new_room = input("Do you want to return to Room V ? (y/n): ")
                if new_room == 'y':
                    print("Returned to Room V...")
                    room = "V"
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 5
                        rightSteps = 5
                        topSteps = 10
                        downSteps = 0
                        continue
                    else:
                        break
        walk_choice = input("Where do you want to walk ?: (l/r/t/d) (e for exit): ")
        if walk_choice == 'l':
            steps = input("How many steps ?: ")
            if int(steps) <= int(leftSteps):
                leftSteps -= int(steps)
                rightSteps += int(steps)
            else:
                print("You can't go ahead...")
            if leftSteps == 10 and rightSteps == 0 and topSteps == 5 and downSteps == 5:
                new_room = input("Do you want to enter Room II ? (y/n): ")
                if new_room == 'y':
                    ahead = input("Do you want to go ahead ? (y/n): ")
                    if ahead == 'y':
                        leftSteps = 0
                        rightSteps = 10
                        topSteps = 5
                        downSteps = 5
                        continue
        elif walk_choice == 'r':
            steps = input("How many steps ?: ")
            if int(steps) <= int(rightSteps):
                leftSteps += int(steps)
                rightSteps -= int(steps)
            else:
                print("You can't go ahead...")
        elif walk_choice == 't':
            steps = input("How many steps ?: ")
            if int(steps) <= int(topSteps):
                topSteps -= int(steps)
                downSteps += int(steps)
            else:
                print("You can't go ahead...")
        elif walk_choice == 'd':
            steps = input("How many steps ?: ")
            if int(steps) <= int(downSteps):
                downSteps -= int(steps)
                topSteps += int(steps)
            else:
                print("You can't go ahead...")
        ahead = input("Do you want to go ahead ? (y/n): ")
