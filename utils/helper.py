import time


def compare(prompt, proprietary_model, open_model):

    print("=" * 80)
    print("PROMPT")
    print(prompt)

    print("\nRunning Proprietary Model...")

    start = time.time()
    p_response = proprietary_model(prompt)
    p_time = round(time.time() - start, 2)

    print("\nRunning Open Source Model...")

    start = time.time()
    o_response = open_model(prompt)
    o_time = round(time.time() - start, 2)

    print("\n" + "=" * 80)

    print("PROPRIETARY RESPONSE\n")
    print(p_response)

    print("\n" + "-" * 80)

    print("OPEN SOURCE RESPONSE\n")
    print(o_response)

    print("\n" + "-" * 80)

    print(f"Gemini Time : {p_time} sec")
    print(f"Phi-3 Time  : {o_time} sec")

    return p_response, o_response