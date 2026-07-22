class Workflow:

    def run(self, steps):

        results = []

        for i, step in enumerate(steps, 1):

            print(f"[{i}] {step}")

            results.append(f"✅ {step}")

        return "\n".join(results)


workflow = Workflow()
