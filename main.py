from flask import Flask, render_template_string

app = Flask(__name__)

perfumes = [
    {
        "name": "9PM Rebel",
        "image": "9pm-rebel.png",
        "price5": 399,
        "price50": 2999,
        "description": "description""A, bold, modern fragrance for evenings, special occasions, and everyday confidence.",
"notes": "Warm spices, fresh citrus, and smooth woody accords.",
"vibe": "Bold, warm, modern"
    },
    {
        "name": "Sunrise",
        "image": "sunrise.png",
        "price5": 399,
        "price50": 2999,
        "description": "Extrait de Parfum • Long-Lasting • 50ml • For Women. Elegant beauty. Timeless sophistication.",
"profile": "Floral • Rose • Powdery • Sweet • Musky",
"notes": "Rose Petals • Jasmine • Fresh Pear • Soft Vanilla • Amber • White Musk",
    },
    {
        "name": "Janan Sport",
        "image": "janan-sport.png",
        "price5": 399,
        "price50": 2999,
        "description": "Extrait de Parfum • Long-Lasting • 50ml • For Men. Fresh energy. Confident presence.",
        "profile": "Fresh • Citrus • Marine • Woody • Musky",
        "notes": "Bergamot • Lemon • Pineapple • Marine Notes • Cedarwood • Musk"},
    {
        "name": "Royal Rose",
        "image": "royal-rose.png",
        "price5": 399,
        "price50": 2999,
        "description": "Extrait de Parfum • Long-Lasting • 50ml • Unisex. Fresh beginnings. Radiant confidence.",
"profile": "Fresh • Citrus • Aromatic • Woody • Clean",
"notes": "Bergamot • Lemon • Mandarin • Aromatic Herbs • Cedarwood • Musk",
    }
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BRAND BY AKRAM | Perfumes</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #fffaf0;
            color: #332719;
        }

        header {
            text-align: center;
            padding: 30px 15px;
            background: #f2e5ce;
        }

        header h1 {
            margin: 0;
            letter-spacing: 3px;
        }

        header p {
            margin-bottom: 0;
        }

        .intro {
            text-align: center;
            padding: 25px 15px;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 22px;
            padding: 20px;
            max-width: 1100px;
            margin: auto;
        }

        .card {
            background: white;
            border: 1px solid #eadcc5;
            border-radius: 12px;
            padding: 18px;
            text-align: center;
            box-shadow: 0 4px 12px #0000000d;
        }

        .card img {
            width: 100%;
            height: 210px;
            object-fit: contain;
        }

        .card h2 {
            margin-bottom: 8px;
        }

        .price {
            font-weight: bold;
            line-height: 1.8;
        }

        .order {
            display: inline-block;
            background: #5c6f43;
            color: white;
            text-decoration: none;
            padding: 11px 18px;
            border-radius: 7px;
            margin-top: 10px;
        }

        .order:hover {
            background: #40512d;
        }
/* Mobile responsive design */
@media (max-width: 600px) {
    header {
        padding: 24px 12px;
    }

    header h1 {
        font-size: 25px;
        letter-spacing: 2px;
        overflow-wrap: anywhere;
    }

    .intro {
        padding: 18px 12px;
    }

    .products {
        grid-template-columns: 1fr;
        gap: 16px;
        padding: 12px;
    }

    .card {
        padding: 16px;
    }

    .card img {
        height: 190px;
        max-width: 100%;
    }

    .order {
        display: block;
        width: 100%;
        padding: 14px 10px;
    }

    footer {
        padding: 22px 14px;
        overflow-wrap: anywhere;
    }
}
        footer {
            text-align: center;
            padding: 25px;
            margin-top: 20px;
            background: #f2e5ce;
        }
    </style>
</head>

<body>
    <header>
        <h1>BRAND BY AKRAM</h1>
        <p>Discover Your Signature Fragrance</p>
    </header>

    <section class="intro">
        <h2>Our Perfume Collection</h2>
        <p>Choose your favourite fragrance and order through WhatsApp.</p>
    </section>

    <main class="products">
        {% for perfume in perfumes %}
        <article class="card">
            <img
                src="{{ url_for('static', filename='images/' ~ perfume.image) }}"
                alt="{{ perfume.name }}"
            >

            <h2>{{ perfume.name }}</h2>

<p>{{ perfume.description }}</p>

{% if perfume.profile %}
<p><strong>Fragrance Profile:</strong><br>
{{ perfume.profile }}</p>
{% endif %}

{% if perfume.notes %}
<p><strong>Key Notes:</strong><br>
{{ perfume.notes }}</p>
{% endif %}

            <div class="price">
                5 ml: Rs. {{ perfume.price5 }}<br>
                50 ml: Rs. {{ perfume.price50 }}
            </div>

            <label for="size-{{ loop.index }}">Choose Size:</label>

<select id="size-{{ loop.index }}" class="size-select">
    <option value="5 ml" data-price="{{ perfume.price5 }}">5 ml - Rs. {{ perfume.price5 }}</option>
    <option value="50 ml" data-price="{{ perfume.price50 }}">50 ml - Rs. {{ perfume.price50 }}</option>
</select>

<a
    class="order"
    href="https://wa.me/923449631521?text={{ ('Assalamualaikum, I want to order ' ~ perfume.name ~ ' - 5 ml - Rs. ' ~ perfume.price5)|urlencode }}"
    target="_blank"
    rel="noopener noreferrer"
    onclick="event.preventDefault(); const s = this.parentElement.querySelector('.size-select'); const o = s.options[s.selectedIndex]; const msg = 'Assalamualaikum, I want to order ' + {{ perfume.name|tojson }} + ' - ' + s.value + ' - Rs. ' + o.dataset.price; window.open('https://wa.me/923001234567?text=' + encodeURIComponent(msg), '_blank');"
>
    Order on WhatsApp
</a>
        </article>
        {% endfor %}
    </main>

    <footer>
    <p>BRAND BY AKRAM</p>
    <p>Thank you for visiting our store!</p>

    <hr>

    <p>
        <strong>Website Developed By: Muhammad Sultan</strong>
    </p>

    <p>Apni website banwana chahte hain?</p>
    <p>Website development ke liye WhatsApp par contact karein.</p>

    <a
        class="order"
        href="https://wa.me/923239009211?text=Assalamualaikum%2C%20mujhe%20website%20banwani%20hai."
        target="_blank"
        rel="noopener noreferrer"
    >
        Contact Developer on WhatsApp
    </a>
</footer>
</body>
</html><
"""


@app.route("/")
def home():
    return render_template_string(PAGE, perfumes=perfumes)


if __name__ == "__main__":
    app.run(debug=True)