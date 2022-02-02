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
                res = subprocess.Popen(["steamlink", "> /dev/null 2>&1 &"], env=dict(os.environ, DISPLAY=":0"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                print("Error starting Steam Link -> " + e + ".")
                success = False 

            if res is None or res.returncode != 0:
                print("Error starting Steam link => Result isn't 0 (" + str(res) + ").")

                success = False

        elif "sl-stop" in request.POST:
            res_one = 0
            res_two = 0

            try:
                res_one = subprocess.Popen(["pkill", "-9", "-f", "steamlink"])
                res_two = subprocess.Popen(["pkill",  "-9", "-f", "streaming_client"])
            except Exception as e:
                print("Error stopping Steam Link => " + e + ".")
                success = False

            if res_one.returncode != 0 or res_two.returncode != 0:
                if res_one is not None and res_one.returncode != 0:
                    print("Error stopping Steam Link => Killing Steam Link's result isn't 0 (" + str(res_one.returncode) + ").")
                elif res_two is not None and res_two.returncode != 0:
                    print("Error stopping Steam Link => Killing Stream Client's result isn't 0 (" + str(res_two.returncode) + ").")
                    
                success = False

    return render(request, 'manager/index.html', {"action": action, "success": success})