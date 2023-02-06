from runner.runner import Runner
from example_blueprints.example import MyBlueprint


def main():
    runner = Runner()
    my_blueprint = MyBlueprint(None)
    runner.run(my_blueprint)


if __name__ == "__main__":
    main()
