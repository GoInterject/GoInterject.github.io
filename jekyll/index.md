---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: custom
landing: true
notoc: true
notags: true
---

<!-- list all posts  -->
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul> 


<!-- {% for post in site.categories[page.category] %}
    <a href="{{ post.url | absolute_url }}">
      {{ post.title }}
    </a>
{% endfor %} -->

## About
<div>
  {% if site.data.newMenu.About[0] %}
<ul>
    {% for item1 in site.data.newMenu.About %}
      <li><a href="{{ item1.url }}">{{ item1.page }}</a>
        {% if item1.subfolderitems[0] %}
          <ul>
            {% for item2 in item1.subfolderitems %}
                <li><a href="{{ item2.url }}">{{ item2.page }}</a>
                  {% if item2.subfolderitems[0] %}
                    <ul>
                      {% for item3 in item2.subfolderitems %}
                          <li><a href="{{ item3.url }}">{{ item3.page }}</a>
                            {% if item3.subfolderitems[0] %}
                              <ul>
                                  {% for item4 in item3.subfolderitems %}
                                      <li><a href="{{ item4.url }}">{{ item4.page }}</a>
                                        {% if item4.subfolderitems[0] %}
                                          <ul>
                                          {% for item5 in item4.subfolderitems %}
                                              <li><a href="{{ item5.url }}">{{ item5.page }}</a></li>
                                          {% endfor %}
                                          </ul>
                                        {% endif %}
                                      </li>
                                  {% endfor %}
                                </ul>
                            {% endif %}
                          </li>
                      {% endfor %}
                    </ul>
                  {% endif %}
                </li>
            {% endfor %}
          </ul>
        {% endif %}
    </li>
      {% endfor %}
  </ul>
  {% endif %}
</div>

## Apps
<div>
  {% if site.data.newMenu.Apps[0] %}
<ul>
    {% for item1 in site.data.newMenu.Apps %}
      <li><a href="{{ item1.url }}">{{ item1.page }}</a>
        {% if item1.subfolderitems[0] %}
          <ul>
            {% for item2 in item1.subfolderitems %}
                <li><a href="{{ item2.url }}">{{ item2.page }}</a>
                  {% if item2.subfolderitems[0] %}
                    <ul>
                      {% for item3 in item2.subfolderitems %}
                          <li><a href="{{ item3.url }}">{{ item3.page }}</a>
                            {% if item3.subfolderitems[0] %}
                              <ul>
                                  {% for item4 in item3.subfolderitems %}
                                      <li><a href="{{ item4.url }}">{{ item4.page }}</a>
                                        {% if item4.subfolderitems[0] %}
                                          <ul>
                                          {% for item5 in item4.subfolderitems %}
                                              <li><a href="{{ item5.url }}">{{ item5.page }}</a></li>
                                          {% endfor %}
                                          </ul>
                                        {% endif %}
                                      </li>
                                  {% endfor %}
                                </ul>
                            {% endif %}
                          </li>
                      {% endfor %}
                    </ul>
                  {% endif %}
                </li>
            {% endfor %}
          </ul>
        {% endif %}
    </li>
      {% endfor %}
  </ul>
  {% endif %}
</div>


## GetStarted
<div>
  {% if site.data.newMenu.GetStarted[0] %}
<ul>
    {% for item1 in site.data.newMenu.GetStarted %}
      <li><a href="{{ item1.url }}">{{ item1.page }}</a>
        {% if item1.subfolderitems[0] %}
          <ul>
            {% for item2 in item1.subfolderitems %}
                <li><a href="{{ item2.url }}">{{ item2.page }}</a>
                  {% if item2.subfolderitems[0] %}
                    <ul>
                      {% for item3 in item2.subfolderitems %}
                          <li><a href="{{ item3.url }}">{{ item3.page }}</a>
                            {% if item3.subfolderitems[0] %}
                              <ul>
                                  {% for item4 in item3.subfolderitems %}
                                      <li><a href="{{ item4.url }}">{{ item4.page }}</a>
                                        {% if item4.subfolderitems[0] %}
                                          <ul>
                                          {% for item5 in item4.subfolderitems %}
                                              <li><a href="{{ item5.url }}">{{ item5.page }}</a></li>
                                          {% endfor %}
                                          </ul>
                                        {% endif %}
                                      </li>
                                  {% endfor %}
                                </ul>
                            {% endif %}
                          </li>
                      {% endfor %}
                    </ul>
                  {% endif %}
                </li>
            {% endfor %}
          </ul>
        {% endif %}
    </li>
      {% endfor %}
  </ul>
  {% endif %}
</div>


## Index
<div>
  {% if site.data.newMenu.Index[0] %}
<ul>
    {% for item1 in site.data.newMenu.Index %}
      <li><a href="{{ item1.url }}">{{ item1.page }}</a>
        {% if item1.subfolderitems[0] %}
          <ul>
            {% for item2 in item1.subfolderitems %}
                <li><a href="{{ item2.url }}">{{ item2.page }}</a>
                  {% if item2.subfolderitems[0] %}
                    <ul>
                      {% for item3 in item2.subfolderitems %}
                          <li><a href="{{ item3.url }}">{{ item3.page }}</a>
                            {% if item3.subfolderitems[0] %}
                              <ul>
                                  {% for item4 in item3.subfolderitems %}
                                      <li><a href="{{ item4.url }}">{{ item4.page }}</a>
                                        {% if item4.subfolderitems[0] %}
                                          <ul>
                                          {% for item5 in item4.subfolderitems %}
                                              <li><a href="{{ item5.url }}">{{ item5.page }}</a></li>
                                          {% endfor %}
                                          </ul>
                                        {% endif %}
                                      </li>
                                  {% endfor %}
                                </ul>
                            {% endif %}
                          </li>
                      {% endfor %}
                    </ul>
                  {% endif %}
                </li>
            {% endfor %}
          </ul>
        {% endif %}
    </li>
      {% endfor %}
  </ul>
  {% endif %}
</div>


## Portal
<div>
  {% if site.data.newMenu.Index[0] %}
<ul>
    {% for item1 in site.data.newMenu.Index %}
      <li><a href="{{ item1.url }}">{{ item1.page }}</a>
        {% if item1.subfolderitems[0] %}
          <ul>
            {% for item2 in item1.subfolderitems %}
                <li><a href="{{ item2.url }}">{{ item2.page }}</a>
                  {% if item2.subfolderitems[0] %}
                    <ul>
                      {% for item3 in item2.subfolderitems %}
                          <li><a href="{{ item3.url }}">{{ item3.page }}</a>
                            {% if item3.subfolderitems[0] %}
                              <ul>
                                  {% for item4 in item3.subfolderitems %}
                                      <li><a href="{{ item4.url }}">{{ item4.page }}</a>
                                        {% if item4.subfolderitems[0] %}
                                          <ul>
                                          {% for item5 in item4.subfolderitems %}
                                              <li><a href="{{ item5.url }}">{{ item5.page }}</a></li>
                                          {% endfor %}
                                          </ul>
                                        {% endif %}
                                      </li>
                                  {% endfor %}
                                </ul>
                            {% endif %}
                          </li>
                      {% endfor %}
                    </ul>
                  {% endif %}
                </li>
            {% endfor %}
          </ul>
        {% endif %}
    </li>
      {% endfor %}
  </ul>
  {% endif %}
</div>
