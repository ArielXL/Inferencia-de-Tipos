class Main inherits IO {
    main() : AUTO_TYPE {
        let x : AUTO_TYPE <- 3 + 2 in
            case x of
                y : Int => out_string("Ok");
            esac
    };
};

