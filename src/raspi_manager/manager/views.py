from django.shortcuts import render

import os
import subprocess

def perform_steam_link(start = True):
    res = None

    if start:
        try:
            tmp = subprocess.Popen(["steamlink &"], shell = True, start_new_session = True, env = dict(os.environ, DISPLAY=":0"), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        except Exception as e:
            print("Error starting Steam Link -> " + str(e) + ".")
            
            return res

        tmp.wait()

        res = tmp.returncode
    else:
        res_one = None

        try:
            res_one = subprocess.Popen(["../../scripts/stop_steamlink.sh"], shell = False, start_new_session = True)
        except Exception as e:
            print("Error stopping Steam Link => " + str(e) + ".")
            
            return res

        res_one.wait()

        res = res_one.returncode

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