set PATH /usr/lib/dart/bin $PATH
set -x PATH $HOME/.anyenv/bin $PATH
eval (anyenv init - | source)

starship init fish | source
