from django.shortcuts import render

import os
import subprocess

def manage(request):
    action = False
    success = True

    # Check for action.
    if request.method == "POST":
        action = True

        # Check if Steam link start is set.
        if "sl-start" in request.POST:
            res = 0

            try:
                res = subprocess.run(["steamlink", "> /dev/null 2>&1 &"], env=dict(os.environ, DISPLAY=":0"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                print("Error starting Steam Link -> " + e + ".")
                success = False 

            if res != 0:
                print("Error starting Steam link => Result isn't 0 (" + str(res) + ").")

        elif "sl-stop" in request.POST:
            res_one = 0
            res_two = 0

            try:
                res_one = os.system("pkill -9 -f steamlink")
                res_two = os.system("pkill -9 -f streaming_client")
            except Exception as e:
                print("Error stopping Steam Link => " + e + ".")
                success = False


            if res_one != 0 or res_two != 0:
                if res_one != 0:
                    print("Error stopping Steam Link => Killing Steam Link's result isn't 0 (" + str(res_one) + ").")
                elif res_two != 0:
                    print("Error stopping Steam Link => Killing Stream Client's result isn't 0 (" + str(res_two) + ").")
                success = False

    return render(request, 'manager/index.html', {"action": action, "success": success})