# Run server
python -m uvicorn web.server:app --reload --port 8000


Khác biệt khi dùng uvicorn ... vs python -m uvicorn ...

uvicorn ...
Khi bạn gõ thẳng uvicorn, shell sẽ tìm một file thực thi tên uvicorn trong PATH.
File đó thực chất chỉ là một script wrapper được cài vào .venv/bin/uvicorn.
Nó gọi Python, nhưng trong một số tình huống (PATH lẫn lộn, nhiều Python, nhiều venv), script này có thể chạy sai interpreter → dẫn đến lỗi như "No module named 'fastapi'".

python -m uvicorn ...
Khi chạy với python -m, bạn bắt buộc uvicorn phải chạy bằng chính interpreter mà bạn gọi (.venv/bin/python).
Nó sẽ tìm package uvicorn trong sys.path của interpreter đó và chạy module uvicorn.__main__.
Vì vậy đảm bảo chắc chắn dùng đúng Python và đúng thư viện đã cài trong venv hiện tại.