This is a realistic-looking repository that demonstrates how secrets can accidentally end up in code — and how GitHub Secret Scanning helps detect them.

⚠️ **All secrets in this repo are FAKE and non-functional**.  
They are included **only for educational purposes** to show how secret scanning works.

## Usage

```bash
pip install -r requirements.txt
python word_finder.py --file sample_data.txt --word "password"
