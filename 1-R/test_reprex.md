This template demonstrates many of the bells and whistles of the `reprex::reprex_document()` output format. The YAML sets many options to non-default values, such as using `#;-)` as the comment in front of output.

## Code style

Since `style` is `TRUE`, this difficult-to-read code (look at the `.Rmd` source file) will be restyled according to the Tidyverse style guide when it’s rendered. Whitespace rationing is not in effect!

``` r
x <- 1
y <- 2
z <- x + y
z
#;-) [1] 3
```

## Quiet tidyverse

The tidyverse meta-package is quite chatty at startup, which can be very useful in exploratory, interactive work. It is often less useful in a reprex, so by default, we suppress this.

However, when `tidyverse_quiet` is `FALSE`, the rendered result will include a tidyverse startup message about package versions and function masking.

``` r
library(tidyverse)
#;-) ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──
#;-) ✔ ggplot2 3.3.6     ✔ purrr   0.3.4
#;-) ✔ tibble  3.1.7     ✔ dplyr   1.0.9
#;-) ✔ tidyr   1.2.0     ✔ stringr 1.4.0
#;-) ✔ readr   2.0.0     ✔ forcats 0.5.1
#;-) ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
#;-) ✖ dplyr::filter() masks stats::filter()
#;-) ✖ dplyr::lag()    masks stats::lag()
```

## Chunks in languages other than R

Remember: knitr supports many other languages than R, so you can reprex bits of code in Python, Ruby, Julia, C++, SQL, and more. Note that, in many cases, this still requires that you have the relevant external interpreter installed.

Let’s try Python!

``` python
x = 'hello, python world!'
print(x.split(' '))
#;-) ['hello,', 'python', 'world!']
```

And bash!

``` bash
echo "Hello Bash!";
pwd;
ls | head;
#;-) Hello Bash!
#;-) /d/jianguo/myvscode
#;-) hello.jl
#;-) Program_area.jl
#;-) test.jl
#;-) test.py
#;-) test.R
#;-) test.rmd
#;-) test_reprex.Rmd
#;-) test_reprex_std_out_err.txt
```

Write a function in C++, use Rcpp to wrap it and …

``` cpp
#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
NumericVector timesTwo(NumericVector x) {
  return x * 2;
}
```

then immediately call your C++ function from R!

``` r
timesTwo(1:4)
#;-) [1] 2 4 6 8
```

## Standard output and error

Some output that you see in an interactive session is not actually captured by rmarkdown, when that same code is executed in the context of an `.Rmd` document. When `std_out_err` is `TRUE`, `reprex::reprex_render()` uses a feature of `callr:r()` to capture such output and then injects it into the rendered result.

Look for this output in a special section of the rendered document (and notice that it does not appear right here).

``` r
system2("echo", args = "Output that would normally be lost")
```

## Session info

Because `session_info` is `TRUE`, the rendered result includes session info, even though no such code is included here in the source document.

<details style="margin-bottom:10px;">
<summary>
Standard output and standard error
</summary>

``` sh
running: bash  -c "echo \"Hello Bash!\";
pwd;
ls | head;"
Building shared library for Rcpp code chunk...
Output that would normally be lost
```

</details>
<details style="margin-bottom:10px;">
<summary>
Session info
</summary>

``` r
sessioninfo::session_info()
#;-) ─ Session info ───────────────────────────────────────────────────────────────
#;-)  setting  value
#;-)  version  R version 4.2.1 (2022-06-23 ucrt)
#;-)  os       Windows 10 x64 (build 19044)
#;-)  system   x86_64, mingw32
#;-)  ui       RTerm
#;-)  language (EN)
#;-)  collate  Chinese (Simplified)_China.utf8
#;-)  ctype    Chinese (Simplified)_China.utf8
#;-)  tz       Asia/Taipei
#;-)  date     2022-10-18
#;-)  pandoc   2.14.1 @ C:/PROGRA~1/Pandoc/ (via rmarkdown)
#;-) 
#;-) ─ Packages ───────────────────────────────────────────────────────────────────
#;-)  package     * version date (UTC) lib source
#;-)  assertthat    0.2.1   2019-03-21 [1] CRAN (R 4.0.2)
#;-)  backports     1.4.1   2021-12-13 [1] CRAN (R 4.2.0)
#;-)  broom         1.0.0   2022-07-01 [1] CRAN (R 4.2.1)
#;-)  cellranger    1.1.0   2016-07-27 [1] CRAN (R 4.0.2)
#;-)  cli           3.3.0   2022-04-25 [1] CRAN (R 4.2.1)
#;-)  colorspace    2.0-3   2022-02-21 [1] CRAN (R 4.2.1)
#;-)  crayon        1.5.1   2022-03-26 [1] CRAN (R 4.2.1)
#;-)  DBI           1.1.0   2019-12-15 [1] CRAN (R 4.0.2)
#;-)  dbplyr        2.1.1   2021-04-06 [1] CRAN (R 4.1.0)
#;-)  digest        0.6.29  2021-12-01 [1] CRAN (R 4.2.1)
#;-)  dplyr       * 1.0.9   2022-04-28 [1] CRAN (R 4.2.1)
#;-)  ellipsis      0.3.2   2021-04-29 [1] CRAN (R 4.1.0)
#;-)  evaluate      0.15    2022-02-18 [1] CRAN (R 4.2.1)
#;-)  fansi         1.0.3   2022-03-24 [1] CRAN (R 4.2.1)
#;-)  forcats     * 0.5.1   2021-01-27 [1] CRAN (R 4.1.0)
#;-)  fs            1.5.0   2020-07-31 [1] CRAN (R 4.0.2)
#;-)  generics      0.1.3   2022-07-05 [1] CRAN (R 4.2.1)
#;-)  ggplot2     * 3.3.6   2022-05-03 [1] CRAN (R 4.2.1)
#;-)  glue          1.6.2   2022-02-24 [1] CRAN (R 4.2.1)
#;-)  gtable        0.3.0   2019-03-25 [1] CRAN (R 4.0.2)
#;-)  haven         2.3.1   2020-06-01 [1] CRAN (R 4.0.2)
#;-)  here          1.0.1   2020-12-13 [1] CRAN (R 4.1.2)
#;-)  hms           1.1.0   2021-05-17 [1] CRAN (R 4.1.0)
#;-)  htmltools     0.5.1.1 2021-01-22 [1] CRAN (R 4.1.0)
#;-)  httr          1.4.2   2020-07-20 [1] CRAN (R 4.0.2)
#;-)  jsonlite      1.8.0   2022-02-22 [1] CRAN (R 4.2.1)
#;-)  knitr         1.39    2022-04-26 [1] CRAN (R 4.2.1)
#;-)  lattice       0.20-45 2021-09-22 [2] CRAN (R 4.2.1)
#;-)  lifecycle     1.0.1   2021-09-24 [1] CRAN (R 4.2.1)
#;-)  lubridate     1.7.10  2021-02-26 [1] CRAN (R 4.1.0)
#;-)  magrittr      2.0.1   2020-11-17 [1] CRAN (R 4.1.0)
#;-)  Matrix        1.3-4   2021-06-01 [1] CRAN (R 4.1.0)
#;-)  modelr        0.1.8   2020-05-19 [1] CRAN (R 4.0.2)
#;-)  munsell       0.5.0   2018-06-12 [1] CRAN (R 4.0.2)
#;-)  pillar        1.7.0   2022-02-01 [1] CRAN (R 4.2.1)
#;-)  pkgconfig     2.0.3   2019-09-22 [1] CRAN (R 4.0.2)
#;-)  png           0.1-7   2013-12-03 [1] CRAN (R 4.1.1)
#;-)  purrr       * 0.3.4   2020-04-17 [1] CRAN (R 4.0.2)
#;-)  R.cache       0.16.0  2022-07-21 [1] CRAN (R 4.2.1)
#;-)  R.methodsS3   1.8.2   2022-06-13 [1] CRAN (R 4.2.0)
#;-)  R.oo          1.25.0  2022-06-12 [1] CRAN (R 4.2.0)
#;-)  R.utils       2.12.0  2022-06-28 [1] CRAN (R 4.2.1)
#;-)  R6            2.5.1   2021-08-19 [1] CRAN (R 4.2.1)
#;-)  rappdirs      0.3.3   2021-01-31 [1] CRAN (R 4.1.0)
#;-)  Rcpp          1.0.9   2022-07-08 [1] CRAN (R 4.2.1)
#;-)  readr       * 2.0.0   2021-07-20 [1] CRAN (R 4.1.0)
#;-)  readxl        1.3.1   2019-03-13 [1] CRAN (R 4.0.2)
#;-)  reprex        2.0.1   2021-08-05 [1] CRAN (R 4.1.0)
#;-)  reticulate    1.24    2022-01-26 [1] CRAN (R 4.1.2)
#;-)  rlang         1.0.3   2022-06-27 [1] CRAN (R 4.2.1)
#;-)  rmarkdown     2.14    2022-04-25 [1] CRAN (R 4.2.0)
#;-)  rprojroot     2.0.3   2022-04-02 [1] CRAN (R 4.2.1)
#;-)  rstudioapi    0.13    2020-11-12 [1] CRAN (R 4.1.0)
#;-)  rvest         1.0.1   2021-07-26 [1] CRAN (R 4.1.0)
#;-)  scales        1.2.0   2022-04-13 [1] CRAN (R 4.2.1)
#;-)  sessioninfo   1.2.2   2021-12-06 [1] CRAN (R 4.2.1)
#;-)  stringi       1.7.8   2022-07-11 [1] CRAN (R 4.2.1)
#;-)  stringr     * 1.4.0   2019-02-10 [1] CRAN (R 4.0.2)
#;-)  styler        1.7.0   2022-03-13 [1] CRAN (R 4.2.1)
#;-)  tibble      * 3.1.7   2022-05-03 [1] CRAN (R 4.2.1)
#;-)  tidyr       * 1.2.0   2022-02-01 [1] CRAN (R 4.2.1)
#;-)  tidyselect    1.1.2   2022-02-21 [1] CRAN (R 4.2.1)
#;-)  tidyverse   * 1.3.1   2021-04-15 [1] CRAN (R 4.1.0)
#;-)  tzdb          0.1.2   2021-07-20 [1] CRAN (R 4.1.0)
#;-)  utf8          1.2.2   2021-07-24 [1] CRAN (R 4.2.1)
#;-)  vctrs         0.4.1   2022-04-13 [1] CRAN (R 4.2.1)
#;-)  withr         2.5.0   2022-03-03 [1] CRAN (R 4.2.1)
#;-)  xfun          0.31    2022-05-10 [1] CRAN (R 4.2.1)
#;-)  xml2          1.3.2   2020-04-23 [1] CRAN (R 4.0.2)
#;-)  yaml          2.3.5   2022-02-21 [1] CRAN (R 4.2.0)
#;-) 
#;-)  [1] D:/MyR_Lib4
#;-)  [2] C:/Program Files/R/R-4.2.1/library
#;-) 
#;-) ─ Python configuration ───────────────────────────────────────────────────────
#;-)  python:         C:/Users/xingfu_2/AppData/Local/Programs/Python/Python39/python.exe
#;-)  libpython:      C:/Users/xingfu_2/AppData/Local/Programs/Python/Python39/python39.dll
#;-)  pythonhome:     C:/Users/xingfu_2/AppData/Local/Programs/Python/Python39
#;-)  version:        3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
#;-)  Architecture:   64bit
#;-)  numpy:          D:/mypy_Lib/Python39/site-packages/numpy
#;-)  numpy_version:  1.23.4
#;-) 
#;-) ──────────────────────────────────────────────────────────────────────────────
```

</details>
