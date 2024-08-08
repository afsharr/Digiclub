 Digiclub

Reward Management System
Overview

The Reward Management System is designed to allow users to redeem various types of rewards using their accumulated points. This system includes functionalities for managing discount codes, raffle chances, free products, and conditional cash rewards.
Features

    Point Management: Track and manage user points.
    Reward Types:
        Raffle Chances: Users can enter raffles using points.
        Discount Codes: Apply discount codes for specific product categories.
        Conditional Discount Codes: Apply discounts based on purchase thresholds and conditions.
        Free Products: Redeem products for free using points.
        Conditional Cash Rewards: Get cash discounts based on purchase conditions.

Installation
Prerequisites

    Python 3.8+
    Django 3.2+
    Virtualenv (optional but recommended)

Steps

    Clone the Repository

    bash

git clone https://github.com/afsharr/digiclub.git
cd reward-management-system

Set Up Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

Apply Migrations

bash

python manage.py migrate

Run the Development Server

bash

python manage.py runserver

Access the Admin Interface

Create a superuser if you haven’t already:

bash

    python manage.py createsuperuser

    You can then access the admin interface at http://127.0.0.1:8000/admin/ and manage your rewards and points.

Usage
Admin Interface

    Raffle Chances: Add, edit, or delete raffle chances.
    Discount Codes: Manage discount codes including validity and product categories.
    Conditional Discount Codes: Configure discount codes with purchase thresholds and conditions.
    Free Products: Manage products that can be redeemed for free.
    Conditional Cash Rewards: Set up cash discounts with conditions based on purchase amounts.

API (if applicable)

Provide details on how to interact with the system via API, if available. Include example requests and responses.
Contributing

Contributions are welcome! Please follow the contribution guidelines for submitting pull requests and reporting issues.
License

This project is licensed under the MIT License.
Contact

For questions or support, please contact the.unique.afshar@gmail.com.
