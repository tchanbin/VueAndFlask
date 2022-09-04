import request from '@/utils/request'

export function login(data) {
  return request({
    // url: '/vue-admin-template/user/login',这个地方通过auth使用authbasic 加密，
    // basic 64加密，在请求头部添加Authorization=Basic YWRtaW46MTIzNDU2
    url: 'api/login',
    method: 'post',
    auth: { username: data['username'], password: data['password'] }

  })
}

export function getInfo(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: 'api/info',
    method: 'post',
    // 下面auth处的第一个参数名字必须为username，这样子他才能找到并替你将token进行basic 64加密,token进入@auth.verypassord 验证
    auth: { username: token }
    // params: { token }
  })
}

export function logout(token) {
  return request({
    url: 'api/logout',
    method: 'post',
    auth: { username: token }
  })
}
