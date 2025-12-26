<h1 align="center">Jobs Parser Telegram (MTProto)</h1>

A simple parser of jobs from Telegram for further processing or analysis.

---

##  ▸｜Requirements

- Python 3.11

---

##  ▸｜Installing

1. Clone the repository:

```bash
git clone https://github.com/Vludd/jobs-parser-tg.git
cd jobs-parser-tg
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
```

3. Set dependencies:

```bash
python -m pip install -r requirements.txt   # Linux / Mac
pip install -r requirements.txt             # Windows
```

4. Clone .env.example to .env and configure it:
```bash
cp .env.example .env
```
`API_ID`, `API_HASH` - required config parameters for the application to work

5. Customize `app/config/config.json` to your needs:
- `targets:channels` - specify the **Telegram channels** to parse. Supported options:
    - `"@channel_name"` - channel name
    - `123456789` - channel ID (see description)
- `targets:bots` - specify the Telegram bots to parse. **(Not supported)**
- `filter:whitelist` - search only jobs that **include** at least one item in this list. Specify the **score** value next to the parameter to control the priority of the items
- `filter:blacklist` - **ignore** a found job if it includes at least one item from this list
- `filter:min_score` - the **minimum value** at which the jobs found will be taken into account on a white sheet
- `filter:techstack` - control the **spellings** of each stack: `"stack": ["spellings", ...]`

6. After configuring app/config/config.json, specify SEND_TO_CHANNEL_ID in `.env` file. Supported options: 
    - @my_public_channel - only public channels
    - 1234567890 - public/private channel ID

> If this is a **public** channel, specify PRIVATE_CHANNEL=False to prevent the client from attempting to send messages to the private channel.
> If this is a **private** channel - PRIVATE_CHANNEL=True or leave blank

##  ▸｜Run

```bash
python app.main
```

##  ▸｜Using
Launch and listen to notifications from Telegram

---

## ▸｜Tasklist
- [x] Support for Channels parsing
- [x] White List & Blacklist Filtering
- [ ] Support for Bot parsing
- [ ] Data export
- [ ] Integrate ML to improve parsing efficiency

---

## ▸｜License
The project is distributed under the mit License. For more information, see the LICENSE file.


