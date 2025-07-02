from dummy_project.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from Dummy Project!" in captured.out
