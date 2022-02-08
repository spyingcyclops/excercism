input_data = ["happy", "manageable", "fold", "eaten", "avoidable", "usual"]
result_data = [f"un{item}" for item in input_data]
number_of_variants = range(1, len(input_data) + 1)

for variant, word, result in zip(number_of_variants, input_data, result_data):
    with self.subTest(f"variation #{variant}", word=word, result=result):
        self.assertEqual(
            add_prefix_un(word),
            result,
            msg=f"Expected: {result} but got a different word instead.",
        )

