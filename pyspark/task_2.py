from pyspark.sql import SparkSession
from dotenv import load_dotenv


def main():

    load_dotenv()

    spark = (
        SparkSession.builder.master("local")
        .appName("ProductCategory")
        .getOrCreate()
    )

    products_data = [
        (1, "Product1"),
        (2, "Product2"),
        (3, "Product3"),
        (4, "Product4"),
    ]

    products_df = spark.createDataFrame(
        products_data, ["product_id", "product_name"]
    )

    categories_data = [
        (1, "Category1"),
        (2, "Category2"),
        (3, "Category3"),
    ]

    categories_df = spark.createDataFrame(
        categories_data, ["category_id", "category_name"]
    )

    # Связи между продуктами и категориями
    product_category_data = [
        (1, 1),
        (2, 1),
        (2, 2),
        (3, 3),
    ]

    product_category_df = spark.createDataFrame(
        product_category_data, ["product_id", "category_id"]
    )

    # Присоединение продуктов к категориям
    product_category_joined_df = (
        product_category_df.join(products_df, "product_id")
        .join(categories_df, "category_id")
        .select("product_name", "category_name")
    )

    print("Пары «Имя продукта – Имя категории»:")
    product_category_joined_df.show()

    # Поиск продуктов, у которых нет категорий
    products_with_no_category_df = products_df.join(
        product_category_df, "product_id", "left_anti"
    )

    print("Продукты без категорий:")
    products_with_no_category_df.show()


if __name__ == "__main__":
    main()
