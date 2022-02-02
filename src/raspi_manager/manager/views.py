from django.shortcuts import render

import os
import subprocess

def perform_steam_link(start = True):
    res = None

    if start:
        try:
            tmp = subprocess.Popen(["steamlink", "> /dev/null 2>&1 &"], shell = True, env = dict(os.environ, DISPLAY=":0"), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        except Exception as e:
            print("Error starting Steam Link -> " + e + ".")
            
            return res

        res = tmp.retuncode

    else:
        res_one = None
        res_two = None

        try:
            res_one = subprocess.Popen(["pkill", "-9", "-f", "steamlink"])
            res_two = subprocess.Popen(["pkill",  "-9", "-f", "streaming_client"])
        except Exception as e:
            print("Error stopping Steam Link => " + e + ".")
            
            return res

        if res_one.returncode is None or res_one.returncode != 0:
            print("Error stopping Steam Link process.")

            res = res_one.returncode
        elif res_two.returncode is None or res_two.returncode != 0:
            print("Error stopping Steam Link's streaming service.")

            res = res_two.returncode
        else:
            res = 0

    return res

def manage(request):
    action = False
    success = True

    # Check for action.
    if request.method == "POST":
        action = True

        # Check if Steam link start is set.
        if "sl-start" in request.POST:
            res = perform_steam_link()



            if res is None or res != 0:
                print("Error starting Steam Link => Result isn't 0 (" + str(res) + ").")

                success = False

        elif "sl-stop" in request.POST:
            res = perform_steam_link(False)

            if res is None or res != 0:
                print("Error stopping Steam Link => Result isn't 0 (" + str(res) + ").")
                success = False

    return render(request, 'manager/index.html', {"action": action, "success": success})