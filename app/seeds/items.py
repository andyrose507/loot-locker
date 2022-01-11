from app.models import db, Item


# Adds a demo user, you can add other users here if you want
def seed_items():
    bow = Item(
        user_id=2,
        name="Ultimate Gandiva",
        description="Bard's bow in the image of a shaper of time.",
        image="https://attire.jp/wp-content/uploads/2021/09/ffxiv_20210910_012025_252.jpg",
        price=60000,
        stock=3,
        created_at="Sat, 08 Jan 2022 19:26:00 GMT",
        updated_at="Sat, 08 Jan 2022 19:26:00 GMT",
    )
    helm = Item(
        user_id=2,
        name="Law's Order Helm of Maiming",
        description="Final Fantasy XII was a masterpiece and you can't tell me otherwise.",
        image="http://attire.jp/wp-content/uploads/2021/06/ffxiv_20210603_140940_485.png",
        price=5000,
        stock=8,
        created_at="Sat, 08 Jan 2022 19:28:00 GMT",
        updated_at="Sat, 08 Jan 2022 19:28:00 GMT",
    )
    minion = Item(
        user_id=3,
        name="Minion of Light",
        description="Tiny explosions.",
        image="https://pbs.twimg.com/media/FHYhfHZXIAcC6aI?format=jpg&name=large",
        price=1099,
        stock=10,
        created_at="Sat, 08 Jan 2022 19:30:00 GMT",
        updated_at="Sat, 08 Jan 2022 19:30:00 GMT",
    )
    fantasia = Item(
        user_id=1,
        name="Phial of Fantasia",
        description="It's all cat girls? Always has been.",
        image="https://onlinestore-img.finalfantasyxiv.com/onlinestore/item/2048d09293f96c8fe0ec4746a79572aed973962cf008f2b37506566ba727db1c/0000/b8fd228346654a8cee3e920c32017493f0e99cf8266b6d9e1e9b30f7ed245eab_m_detail.jpg",
        price=700,
        stock=42,
        created_at="Sat, 08 Jan 2022 19:32:00 GMT",
        updated_at="Sat, 08 Jan 2022 19:32:00 GMT",
    )
    gunblade = Item(
        user_id=1,
        name="Squall's Gunblade Replica",
        description="Whatever.",
        image="https://assets.vg247.com/current//2017/12/Final_Fantasy_8_Gunblade.jpg",
        price=80000,
        stock=1,
        created_at="Sat, 08 Jan 2022 19:34:00 GMT",
        updated_at="Sat, 08 Jan 2022 19:34:00 GMT",
    )

    db.session.add(bow)
    db.session.add(helm)
    db.session.add(minion)
    db.session.add(fantasia)
    db.session.add(gunblade)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_items():
    db.session.execute("TRUNCATE items RESTART IDENTITY CASCADE;")
    db.session.commit()
