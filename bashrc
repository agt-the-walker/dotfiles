# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='\u@\h:\w\$ '

shopt -s checkwinsize

export CHROME_BIN=google-chrome-stable
export EDITOR=vim
export HISTSIZE=100000
export JAPANESE_TOOLS=~/src/git/Japanese-Tools

. ~/.bash_aliases

# inspired from /usr/share/doc/pkgfile/command-not-found.bash and
#  ~/src/git/jp-utils/lib/command-not-found
command_not_found_handle () {
  local pkgs cmd=$1
  if [[ "$cmd" = [[:ascii:]]* ]]; then
    mapfile -t pkgs < <(pkgfile -bv -- "$cmd" 2>/dev/null)
    if (( ${#pkgs[*]} )); then
      printf '%s may be found in the following packages:\n' "$cmd"
      printf '  %s\n' "${pkgs[@]}"
      return 0
    else
      printf "bash: $(gettext bash "%s: command not found")\n" "$cmd" >&2
      return 127
    fi
  else
    jm "$cmd"
  fi
}
