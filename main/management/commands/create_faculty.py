import binascii
import os
from django.core.management.base import BaseCommand

from main.models import Faculty


def generate_secret_key():
    return binascii.hexlify(os.urandom(16)).decode()


class Command(BaseCommand):
    help = 'Update secret_key for existing logs'

    def handle(self, *args, **kwargs):
        from main.models import Faculty

        data = [
            {
                "name": "PEDIATRICS",
                "short_name": "PED",
                "direction": "MEDICINES"
            },
            {
                "name": "NURSING INFORMATION",
                "short_name": "NRS",
                "direction": "MEDICINES"
            },
            {
                "name": "GENERAL MEDICINE",
                "short_name": "MED",
                "direction": "MEDICINES"
            },
            {
                "name": "DENTISTRY",
                "short_name": "DNT",
                "direction": "MEDICINES"
            },
            {
                "name": "BEAUTY AESTHETICS",
                "short_name": "BAT",
                "direction": "ARTS"
            },
            {
                "name": "PAINTING",
                "short_name": "PNG",
                "direction": "ARTS"
            },
            {
                "name": "PRE-SCHOOL EDUCATION",
                "short_name": "PRE",
                "direction": "EDUCATION"
            },
            {
                "name": "PRIMARY EDUCATION",
                "short_name": "PED",
                "direction": "EDUCATION"
            },
            {
                "name": "KOREAN PHILOLOGY",
                "short_name": "KOR",
                "direction": "EDUCATION"
            },
            {
                "name": "ENGLISH EDUCATION",
                "short_name": "ENG",
                "direction": "EDUCATION"
            },
            {
                "name": "SPECIAL PEDAGOGY",
                "short_name": "SPD",
                "direction": "EDUCATION"
            },
            {
                "name": "HISTORY",
                "short_name": "HST",
                "direction": "EDUCATION"
            },
            {
                "name": "INTERNATIONAL ECONOMIC RELATIONS",
                "short_name": "IER",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "BUSINESS MANAGEMENT",
                "short_name": "BMA",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "INTERNATIONAL MARKETING",
                "short_name": "IMA",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "TOURISM",
                "short_name": "TOU",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "BANKING",
                "short_name": "BAN",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "FINANCE",
                "short_name": "FIN",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "SPACE TECHNOLOGY",
                "short_name": "SPT",
                "direction": "ENGINEERING"
            },
            {
                "name": "TRAFFIC MANAGEMENT",
                "short_name": "TRM",
                "direction": "ENGINEERING"
            },
            {
                "name": "ARCHITECTURE AND URBAN DESIGN",
                "short_name": "AUD",
                "direction": "ENGINEERING"
            },
            {
                "name": "RENEWABLE ENERGY",
                "short_name": "REN",
                "direction": "ENGINEERING"
            },
            {
                "name": "CIVIL ENGINEERING",
                "short_name": "CEN",
                "direction": "ENGINEERING"
            },
            {
                "name": "INFORMATION SYSTEM ENGINEERING",
                "short_name": "ISE",
                "direction": "ENGINEERING"
            },
            {
                "name": "MECHANICAL ENGINEERING",
                "short_name": "MEN",
                "direction": "ENGINEERING"
            },
            {
                "name": "ELECTRICAL ENGINEERING",
                "short_name": "ELE",
                "direction": "ENGINEERING"
            },
            {
                "name": "ACCOUNTING",
                "short_name": "ACC",
                "direction": "BUSINESS_FINANCE"
            },
            {
                "name": "FASHION DESIGN",
                "short_name": "FAD",
                "direction": "ARTS"
            }
        ]

        for i in data:
            if not Faculty.objects.filter(name=i['name']).exists():
                f = Faculty.objects.create(**i)
                print('Created Faculty {}'.format(f.short_name))
            else:
                print('Faculty {} already exists'.format(i['short_name']))
