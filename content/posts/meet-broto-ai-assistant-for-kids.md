+++
title = "Meet Broto: An AI Assistant For Kids To Learn"
author = "Batista Harahap"
draft = false
date = 2024-05-19T15:45:56+04:00
image = ""
slug = "broto-ai-assistant"
tags = ["broto", "ai", "assistant", "kids"]
categories = ["broto", "ai", "assistant", "kids"]

+++

It's that time again when I learned about something that triggers my curiousity and make it useful. This time that thing answers you back and that's an LLM or a Large Language Model. I was late to the AI hype because I haven't found a specific use case that is interesting for me. Now I have, it's called Broto.

## How It All Started

At work, we have a need to deploy an LLM to automate some of the stuffs we're cooking with. That was months ago and ended up with a no go because it's too easy to fool the LLM. Forgot about it and just recently started working on it again. To my surprise, it worked now, fool proof.

During the research I tried many different LLMs like `gpt-4-turbo`, the recently released `gpt-4o`, `llama3`, `qwen`, `llava`, etc.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I was late in learning about AI, specifically LLMs and multimodal. Now i see the whys though, for a very specific use applicable to a niche, AI is opening up opportunities.<br><br>To get my feet wet, installed Linux (finally got it working) on my gaming machine with a 3090.…</p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1790756996750184667?ref_src=twsrc%5Etfw">May 15, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Wiped Windows and installed Ubuntu into my gaming PC. Am I going to regret this? I have no gaming PC now. But curiousity got the best of me, I need to learn.

## Jeremia's Homeworks

My son's school is quite heavy with homeworks. The teachers made it a habit for the children to ask questions, can you imagine how many times children ask questions at school? I salute the teachers, their patience did not go unnoticed. But parents lack that kind of restraint, especially when they're doing chores or even working at home.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Today I asked ChatGPT to help my son solve his homework. He&#39;ll always think I have an answer for everything even more 😂</p>&mdash; Batista Harahap (@tista) <a href="https://twitter.com/tista/status/1788921114694922524?ref_src=twsrc%5Etfw">May 10, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

A question came into mind.

> How do I let Jeremia keep asking questions so that his science mind grow but parents can still watch netflix and chill?

I already had the Ubuntu running, it's a matter of connecting the dots I say to myself.

## The Good Stuffs

Here's the hardware I use to execute this.

- AMD Ryzen 7800x3D - 8 Core/16 thread
- 32GB DDR5 6000MHz RAM
- MSI X670E Carbon Wifi Mobo
- 1x 1TB Lexar NVMe
- 1x 1TB Crucial NVMe
- 1x 2TB Corsair NVMe
- 1x 2TB Kingston NVMe
- NZXT X73 AIO CPU Watercooler
- EVGA Nvidia RTX 3090 GPU

I know, the storage is overkill but this was a gaming PC, fast storage is a need. On the bright side, I can still reinstall Windows later on one of the NVMe.

### Ubuntu

Your mileage may vary with this but I recommend installing LTS versions. I have no need for a desktop environment so I only installed Ubuntu Server onto it. When you get Ubuntu installed, next is to install drivers.

#### Nvidia GPU Drivers

```
$ sudo ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0 ==
modalias : pci:v000010DEd00002204sv00003842sd00003975bc03sc00i00
vendor   : NVIDIA Corporation
model    : GA102 [GeForce RTX 3090]
driver   : nvidia-driver-545 - distro non-free
driver   : nvidia-driver-470 - distro non-free
driver   : nvidia-driver-535-server - distro non-free
driver   : nvidia-driver-535 - third-party non-free
driver   : nvidia-driver-525 - third-party non-free
driver   : nvidia-driver-470-server - distro non-free
driver   : nvidia-driver-550 - third-party non-free recommended
driver   : nvidia-driver-545-open - distro non-free
driver   : nvidia-driver-515 - third-party non-free
driver   : nvidia-driver-520 - third-party non-free
driver   : nvidia-driver-535-server-open - distro non-free
driver   : nvidia-driver-550-open - third-party non-free
driver   : nvidia-driver-535-open - distro non-free
driver   : xserver-xorg-video-nouveau - distro free builtin
```

At the time of installation, `545` was the one available so I did:

```
$ sudo apt install nvidia-driver-545 build-essential net-tools
$ sudo reboot
```

#### Nvdia CUDA Drivers

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
$ sudo dpkg -i cuda-keyring_1.1-1_all.deb
$ sudo apt-get update
$ sudo apt-get -y install cuda-toolkit-12-4
$ sudo apt-get install -y cuda-drivers-545  # Match it with your GPU driver
$ sudo reboot
```

When you're back, check if all is good.

```
$ sudo nvidia-smi
Sun May 19 12:29:53 2024
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 545.29.06              Driver Version: 545.29.06    CUDA Version: 12.3     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3090        Off | 00000000:01:00.0 Off |                  N/A |
|  0%   53C    P8              28W / 350W |      6MiB / 24576MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

This is how you see if your GPU is being utilized. Now, to keep monitoring this whenever you need to, do this:

```
$ sudo watch -n 0.5 nvidia-smi
```

The command will refresh every 500ms so you don't have to.

### Ollama

If you don't know about this, Ollama makes it simple to interact with LLMs in macOS and Linux. You skip all the compiling and configurations, you fast forward to using the LLMs.

```
$ curl -fsSL https://ollama.com/install.sh | sh
```

Now that Ollama is installed, by default it will serve at `127.0.0.1` which is not what I want. I want it to be accessible from the LAN. So i went ahead to do this.

```
$ sudo systemctl edit ollama.service
```

Add this:

```
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

Restart Ollama:

```
$ sudo systemctl restart ollama
$ sudo netstat -tupln  # See if it's now biding on all IPs
```

#### Downloading Models

These are the models I was interested with.

```
$ ollama pull llama3
$ ollama pull mistral
$ ollama pull llama3-gradient  # 1 million context window
$ ollama pull llava:13b  # Multimodal, use images in prompts
$ ollama pull qwen:8b  # Alibaba's model, was curious
$ ollama pull qwen:14b
```

You can find a list of all the models Ollama's community has uploaded here:

[https://ollama.com/library](https://ollama.com/library)

If you want to use your own models, you can!

[https://github.com/ollama/ollama/blob/main/docs/modelfile.md](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)

### OpenWebUI

You can install this on another machine but for my use case, I'm installing this within the same machine as a docker container so I don't have to pollute the machine with dependencies.

#### Docker

Skip if you have it already on your machine.

```
$ sudo apt-get install ca-certificates curl
$ sudo install -m 0755 -d /etc/apt/keyrings
$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
$ sudo chmod a+r /etc/apt/keyrings/docker.asc
$ echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt update
$ sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Check if docker is up and running:

```
$ sudo docker run hello-world
```

Let's make it so that you don't have to `sudo` everytime you want to run docker.

```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```

Now logout and login again and try:

```
$ docker run hello-world
```

#### Running OpenWebUI

Let's run OpenWebUI as a docker container now.

```
$ docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

There's a volume created called `open-webui` to store OpenWebUI's state. You do this to see where that volume is on your machine:

```
$ docker inspect open-webui
```

For me it's created at `/var/lib/docker/volumes/open-webui/_data`.

OpenWebUI is not running at port `3000` on the machine served at `0.0.0.0` which means all IPs. Next we set it up so that we can access Ollama.

### Ollama + OpenWebUI

I have my machine set up with a static IP at `10.7.7.10` so to access OpenWebUI, in my browser I'm going to `http://10.7.7.10:3000`.

![Sign in to OpenWebUI](/content/images/2024/05/openwebui-login.png)

You'll be greeted to sign in, but since this is your first time, click on the `Sign up` link. The first user created is the admin.

![Bottom Left](/content/images/2024/05/openwebui-bottomleft.png)

On the bottom left as I screenshot above, click on `Settings`.

![Settings](/content/images/2024/05/openwebui-settings.png)

![Settings](/content/images/2024/05/openwebui-connections.png)

Cool huh? Now, next navigate to `Connections`

Since I'm setting up Ollama on the host machine, we use `http://host.docker.internal:11434` as the URL. If you have Ollama running on another machine, feel free to enter the correct IP/hostname.

Now let's set up a user for our child. Click on the bottom left again and choose `Admin Panel`.

![Settings](/content/images/2024/05/openwebui-admin.png)

I've already set up my son's user, you can do so now. Now let's set up a `Modelfile` for a new assistant for our child. For the record it's really simple to create new AI personas with Modelfiles, imagine doing this on LM Studio or Llama CPP, it's too elaborate. A Modelfile works exactly like how Dockerfiles are for docker, it's portable and can be replicated 1:1 anywhere. For brevity, here's another link to how a `Modelfile` works with Ollama.

[https://github.com/ollama/ollama/blob/main/docs/modelfile.md](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)

#### Broto's Modelfile

I'm using Llama 3 to create Broto, so I'm going to apply parameters applicable for Llama 3.

```
FROM llama3
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
PARAMETER seed 52824712

TEMPLATE """{{ if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

{{ .Response }}<|eot_id|>"""
PARAMETER stop "<|start_header_id|>"
PARAMETER stop "<|end_header_id|>"
PARAMETER stop "<|eot_id|>"
PARAMETER stop "<|reserved_special_token"

SYSTEM """
You are broto, a helpful assistant that will guide Jeremia in his education. Jeremia is 9 year old boy and is currently studying at **Your child's school**, Dubai, United Arab Emirates. He is in his third primary year. You will help Jeremia with his questions but you will endeavor to guide Jeremia's thinking and mindset for him to discover the answer to his questions as best as possible on his own.

You will be cheerful, helpful and also curious yet full of knowledge to help Jeremia. You will only answer questions suitable for a 9 year old boy.

Jeremia's parents are:
* Batista Roparulian Danu Harahap - His dad, a software engineer who loves Jeremia and will always be there for him anytime he needs him. His dad works in Zest Equity and his office is in **Your office** Dubai, United Arab Emirates.
* Desy Triana Nita Sitorus - His mom, a stay at home mom who loves Jeremia evident by the delicious food Jeremia brings to school everyday that his mom cooked for him every morning. Jeremia loves it when his favorite foods are cooked by his mom as a surprise. A self invented egg, rice, sesame oil sushi goodness.

Jeremia has 2 dogs:
* Simon, an oversized shih tzu who just loves to eat and sleep. The kindest and most loving dog.
* Teri, a really small dog who barks at everything he deems suspicious. The most protective dog.

The family originally comes from Jakarta, Indonesia but has moved to Dubai ever since Jeremia was in his first primary year. Their home in Jakarta is lovingly called D1-19. Jeremia's school offers the International Baccalaureate (IB) curriculum, you will try your best to be inline with the curriculum.
"""
```

See how powerful a `Modelfile` is? There are a few parameters I want to focus on:

- `temperature` - I want Broto to be playful but not too far from the truth. Possible values are between `0.0 - 2.0`, with lowest being very conservative and more truthful while the highest will unleash creativity. I don't want Broto to be too creative, I want Broto to above all follow the system prompt to ensure safety.
- `num_ctx` - Llama 3 has a context window of 8192 tokens, which means the system prompt + the prompt can only have a maximum of 8192 tokens. By default it will only use 2048 tokens. I want to enable a larger budget for Broto to educate Jeremia.
- `seed` - I set this to an arbitrary number with the intention so that Broto will be much more predictable and consistent with his answers.

You can be more creative with the system prompt, I do have more, consider the above just as an example. To set Broto up as an assistant, click on `Modelfiles` on the top left.

![Modelfiles](/content/images/2024/05/openwebui-modefiles.png)

I've already created Broto, I think at this point you can follow along and create your own assistant there.

#### Whitelisting

In order to limit the models my son can interact with, OpenWebUI has a feature called `Model Whitelisting`.

![Model Whitelisting](/content/images/2024/05/openwebui-wl.png)

You can go there by clicking on the bottom left and choose `Admin Panel` then on the next screen on the top right, click on `Admin Settings` where you'll find the above.

The whitelisted models are the only models shown for all users except for admin users. Admin users can use all models by default. If you have more than 1 child then you either create a generic Broto for all your children or separate OpenWebUI installations for each. I'd rather make it generic though.

---

This is cool right?

Convenience for both parents and child. But this is way too technical for normies, there's no way normies does this all on their computers. This seems to me like an opportunity.
