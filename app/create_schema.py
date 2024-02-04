from tortoise import Tortoise, run_async

from database.connect import connect


async def main():
    await connect()
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(main())
